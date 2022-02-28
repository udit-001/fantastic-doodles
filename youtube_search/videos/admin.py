from django.contrib import admin
from videos.models import VideoResult, SearchQuery


@admin.register(VideoResult)
class VideoResultAdmin(admin.ModelAdmin):
    list_display = ["title", "published_on"]
    list_filter = ["published_on", "query"]
    ordering = ["-published_on"]


@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ["keyword", "last_fetched_on"]
    readonly_fields = ["keyword", "last_fetched_on"]
