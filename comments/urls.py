from django.urls import path
from .views import CommentCreateView, CommentListView, CommentDeleteView

urlpatterns = [
    path('vlogs/<int:vlog_id>/comments/', CommentCreateView.as_view(), name='comment-add'),
    path('vlogs/<int:vlog_id>/comments/list/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
