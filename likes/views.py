from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from vlogs.models import Vlog
from .models import Like


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_vlog(request, id):
    vlog = get_object_or_404(Vlog, id=id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        vlog=vlog
    )

    if not created:
        return Response(
            {"detail": "Already liked"},
            status=400
        )

    return Response(
        {"detail": "Vlog liked"},
        status=201
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_vlog(request, id):
    vlog = get_object_or_404(Vlog, id=id)

    like = Like.objects.filter(
        user=request.user,
        vlog=vlog
    )

    if not like.exists():
        return Response(
            {"detail": "Not liked yet"},
            status=400
        )

    like.delete()
    return Response(
        {"detail": "Like removed"},
        status=200
    )


@api_view(['GET'])
def vlog_likes(request, id):
    vlog = get_object_or_404(Vlog, id=id)

    return Response(
        {"likes": vlog.likes.count()},
        status=200
    )
