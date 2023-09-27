from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_practices.home.urls')),
    path('', include('django_practices.reports.urls')),
    path('', include('django_practices.crud.urls')),
    path('', include('django_practices.authentication.urls')),
    path('', include('django_practices.emails.urls')),
    path('', include('django_practices.cache.urls')),
    path('', include('django_practices.chart.urls')),
    path('', include('django_practices.inlineform.urls')),
]
