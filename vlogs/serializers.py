from rest_framework import serializers
from .models import Vlog

class VlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Vlog
        fields = ['id', 'title', 'description', 'video_url', 'author', 'created_at']
