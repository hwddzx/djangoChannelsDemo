import queue

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

USER_QUEUE = {}


def home(request):
    uid = request.GET.get('uid')
    USER_QUEUE[uid] = queue.Queue()
    print(USER_QUEUE)
    return render(request, 'long_poll/index.html', {'uid': uid})


class MessageView(View):

    def get(self, request):
        uid = request.GET.get('uid')
        result = {
            'status': True,
            'data': None
        }
        try:
            data = USER_QUEUE[uid].get(timeout=10)
            result['data'] = data
        except queue.Empty:
            result['status'] = False

        return JsonResponse(result)

    def post(self, request):
        msg = request.POST.get('message')
        for _, q in USER_QUEUE.items():
            q.put(msg)
        return JsonResponse({})
