from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings

from videos.utils import preserve_search_results
from videos.models import YoutubeKey

logger = get_task_logger(__name__)


def populate_youtube_keys():
    keys = settings.YOUTUBE_API_KEYS
    for key in keys:
        _, created = YoutubeKey.objects.get_or_create(
            key=key
        )
        if created:
            logger.info("Populated YouTube API Key into database.")


@shared_task
def get_popular_queries():
    keys = settings.YOUTUBE_API_KEYS
    if not YoutubeKey.objects.filter(key__in=keys).exists():
        populate_youtube_keys()

    popular_queries = settings.POPULAR_QUERIES

    for query in popular_queries:
        logger.info(f"Fetching latest videos for query: {query}")
        preserve_search_results.delay(query)
