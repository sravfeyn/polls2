from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World from a viewe")

def sp_index(request):
	return HttpResponse("You are browsing polls/sp/")	