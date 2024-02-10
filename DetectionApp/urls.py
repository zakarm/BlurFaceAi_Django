from django.urls import path
from . import views

urlpatterns = [ 
    # path("", views.index, name="index"),
    path("", views.video_feed, name="video_feed"),
    path('video_feed_page/', views.video_feed_page, name='video_feed_page'),
]