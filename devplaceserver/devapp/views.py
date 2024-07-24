from django.shortcuts import render
from .models import User, Manager
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.decorators import renderer_classes
from django.core import serializers
import datetime
from . import bot
from django.http import JsonResponse
from . import RekasoBot

import threading



def index(request):
    now = datetime.datetime.now()

    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)


@csrf_exempt
def add_user(request):
    try:
        user = User()
        user.name = request.POST.get('name')
        user.contact = request.POST.get('contact')
        user.comment = request.POST.get('comment')
        user.time = str(datetime.datetime.now())
        User.save(user)

        # Отправка сообщения в отдельном потоке
        threading.Thread(target=send_message_in_thread, args=(user,)).start()

        return JsonResponse({
            'status': 'success',
            'message': 'Наши менеджеры скоро свяжутся с вами. Хорошего вам дня!'
        })

    except Exception as e:
        print(e)
        print(request.POST.get('name'))
        print(request.POST.get('contact'))
        try:
            bot.send_lead(request.POST.get('contact'))
        except Exception:
            pass
        return JsonResponse({'status': 'error', 'message': 'Произошла ошибка, попробуйте позже.'})


def send_message_in_thread(user):
    try:
        bot.send_message_lead(user)
    except Exception as e:
        print(f"Error sending message: {e}")
        try:
            bot.send_lead(user.contact)
        except Exception as e:
            print(f"Error sending lead: {e}")


@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_all_users(request):
    serializer = serializers.serialize('json', User.objects.all())
    return HttpResponse(serializer, content_type='application/json')


@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_all_managers(request):
    serializer = serializers.serialize('json', Manager.objects.all())
    return HttpResponse(serializer, content_type='application/json')


@csrf_exempt
def add_rekaso(request):
    RekasoBot.send_order(request.POST.get('name'), request.POST.get('phone'), request.POST.get('tovar'))
    return JsonResponse({})



