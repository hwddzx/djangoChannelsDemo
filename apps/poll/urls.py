from django.urls import path
from apps.poll import views


urlpatterns = [
    path('', views.home, name='home'),
    path('message/', views.message, name='message'),
]
