from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    group = request.GET.get('group')
    return render(request, 'websocket/home.html', locals())

