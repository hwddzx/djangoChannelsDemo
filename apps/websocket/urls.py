from django.urls import path
from apps.websocket import views


urlpatterns = [
    path('home/', views.home, name='home'),
]
