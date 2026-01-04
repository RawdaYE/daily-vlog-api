from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from users.models import User
from .models import Follow
from .serializers import FollowSerializer

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, id):
    user_to_follow = get_object_or_404(User, id=id)
    if user_to_follow == request.user:
        return Response({"detail": "You cannot follow yourself"}, status=400)
    follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    if not created:
        return Response({"detail": "Already following"}, status=400)
    return Response({"detail": f"You are now following {user_to_follow.username}"}, status=201)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, id):
    user_to_unfollow = get_object_or_404(User, id=id)
    try:
        follow = Follow.objects.get(follower=request.user, following=user_to_unfollow)
        follow.delete()
        return Response({"detail": f"You have unfollowed {user_to_unfollow.username}"}, status=200)
    except ObjectDoesNotExist:
        return Response({"detail": "You are not following this user"}, status=400)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list_followers(request, id):
    user = get_object_or_404(User, id=id)
    followers = user.followers.all().values('follower__id', 'follower__username', 'created_at')
    return Response(followers)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def list_following(request, id):
    user = get_object_or_404(User, id=id)
    following = user.following.all().values('following__id', 'following__username', 'created_at')
    return Response(following)
