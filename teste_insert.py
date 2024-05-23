import datetime
from home.models import Question, Choice
from django.utils import timezone

question_name = input('Digite a pergunta: ') # Variavel Criada
qtd_choice = int(input ('Quantas opcoes na pergunta: ')) # Variavel Criada
q = Question(question_text=question_name, pub_date=timezone.now())
q.save() #Salva as informações no banco

for i in range(qtd_choice):
    q.choice_set.create(choice_text=input('digite a alternativa '))
q.save(0)