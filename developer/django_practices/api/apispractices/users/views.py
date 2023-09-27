from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import User
from django.urls import reverse_lazy
from django.shortcuts import render
from django.urls import reverse
from .serializers import UserListSerializer
from .serializers import UserDetailSerializer
from .serializers import UserCreateSerializer
from .serializers import UserUpdateSerializer
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class UserListAPI(ListAPIView):
    serializer_class = UserListSerializer
    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()


class UserDetailAPI(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()


class UserCreateAPI(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UserUpdateAPI(UpdateAPIView):
    #permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class UserDeleteAPI(DestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
