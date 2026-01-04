from django.urls import path
from .views import CommentCreateView, CommentListView, CommentDeleteView

urlpatterns = [
    path('add/', CommentCreateView.as_view(), name='comment-add'),
    path('<int:vlog_id>/', CommentListView.as_view(), name='comment-list'),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
]
