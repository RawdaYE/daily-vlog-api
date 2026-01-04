from rest_framework import generics, permissions
from .models import Vlog
from .serializers import VlogSerializer


class VlogListView(generics.ListCreateAPIView):
    queryset = Vlog.objects.all()
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class VlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vlog.objects.all()
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FeedView(generics.ListAPIView):
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = [f.following.id for f in user.following.all()]
        return Vlog.objects.filter(user__id__in=following_users).order_by('-created_at')
