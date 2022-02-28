from rest_framework import serializers

from videos.models import SearchQuery, VideoResult


class VideoResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoResult
        fields = [
            "title", "description", "link", "thumbnail_url", "published_on"
        ]
