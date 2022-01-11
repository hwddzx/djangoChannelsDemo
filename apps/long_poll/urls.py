from django.urls import path
from apps.long_poll import views


urlpatterns = [
    path('', views.home, name='home'),
    path('message/', views.MessageView.as_view(), name='message'),
]
