from django.http import JsonResponse
from django.shortcuts import render

MESSAGE = []


def home(request):
    return render(request, 'poll/home.html')


def message(request):
    if request.method == 'POST':
        msg = request.POST.get('message')
        MESSAGE.append(msg)
        return JsonResponse({})
    elif request.method == 'GET':

        return JsonResponse({'msg': MESSAGE})
