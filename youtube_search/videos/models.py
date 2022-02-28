from django.db import models

class SearchQuery(models.Model):
    keyword = models.CharField(max_length=200)
    last_fetched_on = models.DateTimeField(null=True)

    def __str__(self):
        return self.keyword

class VideoResult(models.Model):
    query = models.ForeignKey("videos.SearchQuery", on_delete=models.SET_NULL, null=True, related_name="videos")
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    thumbnail_url = models.URLField()
    published_on = models.DateTimeField()

    def __str__(self):
        return self.link
