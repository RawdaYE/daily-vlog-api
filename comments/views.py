from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer
from vlogs.models import Vlog

# ----------------------------
# Generic class-based views
# ----------------------------

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        vlog_id = self.kwargs.get('vlog_id')
        vlog = get_object_or_404(Vlog, id=vlog_id)
        serializer.save(user=self.request.user, vlog=vlog)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        vlog_id = self.kwargs.get('vlog_id')
        return Comment.objects.filter(vlog_id=vlog_id).order_by('-created_at')


class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        comment = super().get_object()
        if comment.user != self.request.user:
            raise permissions.PermissionDenied("You cannot delete this comment.")
        return comment

