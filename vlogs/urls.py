from django.urls import path
from .views import VlogListView, VlogCreateView, VlogDetailView, FeedView

urlpatterns = [
    path('vlogs/', VlogListView.as_view(), name='vlog-list'),
    path('vlogs/', VlogCreateView.as_view(), name='vlog-create'),
    path('vlogs/<int:pk>/', VlogDetailView.as_view(), name='vlog-detail'),
    path('feed/', FeedView.as_view(), name='vlog-feed'),
]
