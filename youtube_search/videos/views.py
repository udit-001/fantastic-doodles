from django.db.models import Q
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from rest_framework import generics

from videos.filters import VideoFilter
from videos.models import VideoResult
from videos.serializers import VideoResultSerializer
from videos.tables import VideoTable


class VideoList(generics.ListAPIView):
    serializer_class = VideoResultSerializer

    def get_queryset(self):
        queryset = VideoResult.objects.order_by("-published_on")
        keyword = self.request.query_params.get('q')
        if keyword is not None:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(description__icontains=keyword))
        return queryset


class VideoTableView(SingleTableMixin, FilterView):
    model = VideoResult
    table_class = VideoTable
    template_name = 'videos/list.html'
    filterset_class = VideoFilter

    def get_queryset(self, **kwargs):
        return VideoResult.objects.select_related("query").all()
