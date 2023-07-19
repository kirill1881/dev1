from django.shortcuts import render
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.decorators import renderer_classes
from django.core import serializers
import datetime


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
    user = User()
    user.name = request.POST.get('name')
    user.contact = request.POST.get('contact')
    user.comment = request.POST.get('comment')
    user.time = str(datetime.datetime.now())
    User.save(user)
    return HttpResponse('item was created')


@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_all_users(request):
    serializer = serializers.serialize('json', User.objects.all())
    return HttpResponse(serializer, content_type='application/json')

