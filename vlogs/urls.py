from django.urls import path
from .views import VlogListView, VlogDetailView, FeedView

urlpatterns = [
    path('vlogs/', VlogListView.as_view(), name='vlog-list'), 
    path('vlogs/<int:pk>/', VlogDetailView.as_view(), name='vlog-detail'),
    path('feed/', FeedView.as_view(), name='vlog-feed'),
]
