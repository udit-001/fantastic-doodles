import django_tables2 as tables
from videos.models import VideoResult


class VideoTable(tables.Table):
    link = tables.columns.URLColumn(text="Watch Video")

    class Meta:
        model = VideoResult
        template_name = "django_tables2/bootstrap.html"
        fields = [
            "title", "link", "published_on"
        ]
        order_by = "-published_on"
