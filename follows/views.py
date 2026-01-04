from rest_framework import generics, permissions
from .models import Follow
from .serializers import FollowSerializer

class FollowCreateView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

class UnfollowDestroyView(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        follower = self.request.user
        following_id = self.kwargs['following_id']
        return Follow.objects.get(follower=follower.id, following=following_id)

class FollowersListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Follow.objects.filter(following=user_id)

class FollowingListView(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Follow.objects.filter(follower=user_id)
