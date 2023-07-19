from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    contact = serializers.CharField(max_length=255)
    comment = serializers.CharField(max_length=255)
    time = serializers.CharField(max_length=255)


    class Meta:
        model = User
        fields = '__all__'
