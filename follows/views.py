from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Follow
from users.models import User

class FollowUserView(APIView):
    def post(self, request, user_id):
        follower = request.user
        try:
            following = User.objects.get(id=user_id)
            if follower == following:
                return Response({"error": "Cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            follow, created = Follow.objects.get_or_create(follower=follower, following=following)
            if created:
                return Response({"message": f"Now following {following.username}"})
            else:
                return Response({"message": "Already following"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(APIView):
    def delete(self, request, user_id):
        follower = request.user
        try:
            following = User.objects.get(id=user_id)
            follow = Follow.objects.filter(follower=follower, following=following)
            if follow.exists():
                follow.delete()
                return Response({"message": f"Unfollowed {following.username}"})
            else:
                return Response({"error": "Not following this user"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
