from rest_framework import serializers
from blog.models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "name", "pwd", 'role')

class RegistSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('id', 'name')