from django.urls import path
from . import views
urlpatterns = [
    path('', views.dash_3, name = 'dash_3'),
]