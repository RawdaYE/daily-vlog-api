from rest_framework import serializers
from .models import Vlog

class VlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vlog
        fields = ['id', 'user', 'content', 'media_url', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
