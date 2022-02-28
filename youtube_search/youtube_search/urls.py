from django.contrib import admin
from django.urls import path
from videos.views import VideoList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', VideoList.as_view())
]
