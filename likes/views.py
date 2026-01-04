from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

class LikeListView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        vlog_id = self.kwargs['vlog_id']
        return Like.objects.filter(vlog=vlog_id)

class LikeDeleteView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
