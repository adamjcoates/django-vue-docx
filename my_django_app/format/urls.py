from django.urls import path

from . import views

app_name='format'
urlpatterns = [
  path('', views.format, name='format'),
  path('format', views.format, name='format')
]