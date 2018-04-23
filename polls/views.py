from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
	return HttpResponse("Hello World from a viewe")

def sp_index(request):
	return HttpResponse("You are browsing polls/sp/")	

def detail(request, question_id):
	questions = Question.objects.filter(id=question_id)
	text = questions[0].question_text
	return HttpResponse(
		"You are looking at {}".format(text)
	)
