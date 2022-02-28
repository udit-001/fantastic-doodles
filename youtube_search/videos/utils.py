from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from googleapiclient import discovery
from httplib2 import Http

from videos.models import SearchQuery, VideoResult

logger = get_task_logger(__name__)


def search_youtube(query, timestamp):
    api_service_name = "youtube"
    api_version = "v3"
    api_key = settings.YOUTUBE_API_KEY

    http = Http(cache=".google_api_cache")
    youtube = discovery.build(
        api_service_name, api_version, developerKey=api_key, http=http)

    request = youtube.search().list(
        q=query,
        part="id,snippet",
        fields="etag,items/id/videoId,items/etag,items/snippet/publishTime,items/snippet/title,items/snippet/thumbnails/medium/url,items/snippet/description",
        maxResults=25,
        order="date",
        type="video",
        publishedAfter=timestamp.isoformat()
    )

    response = request.execute()

    output = []

    if len(response["items"]):
        for item in response["items"]:
            data = {}
            data["link"] = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            data["description"] = item["snippet"]["description"]
            data["title"] = item["snippet"]["title"]
            data["thumbnail_url"] = item["snippet"]["thumbnails"]["medium"]["url"]
            data["published_on"] = parse_datetime(
                item["snippet"]["publishTime"])
            output.append(data)

    return output


@shared_task
def preserve_search_results(query):
    timestamp = timezone.now()
    data = search_youtube(query, timestamp)
    search_query, _ = SearchQuery.objects.get_or_create(
        keyword=query, defaults={"last_fetched_on": timestamp}
    )

    for item in data:
        _, created = VideoResult.objects.get_or_create(
            query=search_query,
            link=item["link"],
            defaults={
                "title": item["title"],
                "description": item["description"],
                "thumbnail_url": item["thumbnail_url"],
                "published_on": item["published_on"],
            },
        )
        if created:
            logger.info(f"Storing new video: {item['link']} for {query}")
