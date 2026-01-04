from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Vlog
from .serializers import VlogSerializer
from follows.models import Follow


class VlogListView(generics.ListAPIView):
    queryset = Vlog.objects.all().order_by('-created_at')
    serializer_class = VlogSerializer
    permission_classes = [permissions.AllowAny]

class VlogCreateView(generics.CreateAPIView):
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vlog.objects.all()
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().user != self.request.user:
            raise permissions.PermissionDenied("You cannot edit this vlog")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise permissions.PermissionDenied("You cannot delete this vlog")
        instance.delete()

class FeedView(generics.ListAPIView):
    serializer_class = VlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_ids = user.following.all().values_list('following__id', flat=True)
        return Vlog.objects.filter(user__id__in=following_ids).order_by('-created_at')
