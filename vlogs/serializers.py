from rest_framework import serializers
from .models import Vlog

class VlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vlog
        fields = ['id', 'user', 'content', 'media_url', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
