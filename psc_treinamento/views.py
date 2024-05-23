""" códigos wiews psc_treinamento"""

from django.http import HttpResponse


def index(request):
    return HttpResponse("Bem vindo a Treinamentos PSC  SOLUÇÕES INTELIGENTES")
# Create your views here.