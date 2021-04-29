# https://docs.djangoproject.com/en/2.2/topics/http/urls/

# https://docs.djangoproject.com/en/3.2/topics/http/views/

from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello world")
    