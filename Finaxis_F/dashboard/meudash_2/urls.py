from django.urls import path
from . import views
urlpatterns = [
    path('', views.dash_2, name = 'dash_2'),
]