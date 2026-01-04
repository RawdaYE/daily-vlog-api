from django.urls import path
from .views import LikeCreateView, LikeListView, LikeDeleteView

urlpatterns = [
    path('add/', LikeCreateView.as_view(), name='like-add'),
    path('<int:vlog_id>/', LikeListView.as_view(), name='like-list'),
    path('delete/<int:pk>/', LikeDeleteView.as_view(), name='like-delete'),
]
