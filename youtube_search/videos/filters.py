import django_filters
from videos.models import VideoResult


class VideoFilter(django_filters.FilterSet):
    class Meta:
        model = VideoResult
        fields = [
            "query"
        ]
