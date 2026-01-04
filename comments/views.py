from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        vlog_id = self.kwargs['vlog_id']
        return Comment.objects.filter(vlog=vlog_id)

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
