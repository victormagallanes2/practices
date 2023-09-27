from django.urls import path
from .views import Swagger


urlpatterns = [
               path('swagger-custom/', Swagger.as_view()),
              ]