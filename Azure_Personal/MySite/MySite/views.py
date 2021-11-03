from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola mundo!")

