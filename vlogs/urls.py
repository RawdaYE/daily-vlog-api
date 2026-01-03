from django.urls import path
from .views import VlogListCreateView, VlogRetrieveUpdateDestroyView, FeedView

urlpatterns = [
    path('', VlogListCreateView.as_view(), name='vlog-list-create'),
    path('<int:pk>/', VlogRetrieveUpdateDestroyView.as_view(), name='vlog-detail'),
    path('feed/', FeedView.as_view(), name='feed'),
]
