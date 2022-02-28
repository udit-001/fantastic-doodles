from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics

from videos.models import VideoResult
from videos.serializers import VideoResultSerializer


class VideoList(generics.ListAPIView):
    serializer_class = VideoResultSerializer

    def get_queryset(self):
        queryset = VideoResult.objects.order_by("-published_on")
        keyword = self.request.query_params.get('q')
        if keyword is not None:
            queryset = queryset.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))
        return queryset
