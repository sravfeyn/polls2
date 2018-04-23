from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question


def index(request):
    return HttpResponse("Hello World from a view")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(
        request,
        "polls/detail.html",
        {"question": question}
    )

