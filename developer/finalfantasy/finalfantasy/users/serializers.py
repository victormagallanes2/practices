from rest_framework.serializers import ModelSerializer
from .models import User


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')