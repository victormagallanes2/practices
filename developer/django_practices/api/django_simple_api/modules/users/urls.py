from django.urls import path
from .views import UserListAPI
from .views import UserDetailAPI
from .views import UserCreateAPI
from .views import UserUpdateAPI
from .views import UserDeleteAPI


urlpatterns = [
               path('users/list/', UserListAPI.as_view()),
               path('users/create/', UserCreateAPI.as_view()),
               path('users/detail/<str:pk>/', UserDetailAPI.as_view()),
               path('users/update/<str:pk>/', UserUpdateAPI.as_view()),
               path('users/delete/<str:pk>/', UserDeleteAPI.as_view()),
              ]
