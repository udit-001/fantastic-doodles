from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings

from videos.utils import preserve_search_results

logger = get_task_logger(__name__)


@shared_task
def get_popular_queries():
    popular_queries = settings.POPULAR_QUERIES
    for query in popular_queries:
        logger.info(f"Fetching latest videos for query: {query}")
        preserve_search_results.delay(query)
