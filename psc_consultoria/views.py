""" códigos wiews psc_consultoria"""

from django.http import HttpResponse


def index(request):
    return HttpResponse("Bem vindo a Consultorias PSC  SOLUÇÕES INTELIGENTES")
# Create your views here.
