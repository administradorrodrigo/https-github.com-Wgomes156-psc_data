""" View uma página do projeto - site"""
from django.http import HttpResponse


def index(request):
    return HttpResponse("bem vindo ao Site Gerenciamento de Projetos PSC")