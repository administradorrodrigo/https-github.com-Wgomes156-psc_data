""" página (views - home) """

from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
" função traz informação de uma qwuestion "

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "home/index.html", context)

# Create your views here - Traz uma informação de uma question.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

" resultado da question  - Traz o resultado da question de uma pergunta "
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

" votar na question - vota"
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)