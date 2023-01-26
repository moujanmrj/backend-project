from rest_framework import serializers
from .models import Url, Requests
from core.models import User


class UrlSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Url
        fields = ['address', 'threshold']

    def create(self, validated_data):
        user_id = self.context['user_id']
        if user_id:
            return Url.objects.create(user_id=user_id, **validated_data)