from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer
from vlogs.models import Vlog

class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        vlog_id = self.kwargs['vlog_id']
        vlog = get_object_or_404(Vlog, id=vlog_id)
        serializer.save(user=self.request.user, vlog=vlog)


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        vlog_id = self.kwargs['vlog_id']
        return Comment.objects.filter(vlog_id=vlog_id)
    

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        comment_id = self.kwargs['pk']
        return get_object_or_404(Comment, id=comment_id, user=self.request.user)