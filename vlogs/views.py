from rest_framework import generics, permissions
from .models import Vlog
from .serializers import VlogSerializer
from follows.models import Follow

class VlogListCreateView(generics.ListCreateAPIView):
    queryset = Vlog.objects.all().order_by('-created_at')
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class VlogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vlog.objects.all()
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedView(generics.ListAPIView):
    serializer_class = VlogSerializer

    def get_queryset(self):
        user = self.request.user
        following_ids = Follow.objects.filter(follower=user).values_list('following_id', flat=True)
        return Vlog.objects.filter(author__in=following_ids).order_by('-created_at')
