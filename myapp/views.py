import random

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, 'index.html')


def get_answer(request):
    # question = request.GET.get('question', None)
    answers = [
        "Hi, how are you?",
        "Ohh... I can't understand what you trying to say. Sorry!",
        "I like to play games... But I don't know how to play!",
        "Sorry if my answers are not relevant. :))",
        "I feel sleepy! :("]
    answer = {'answer': answers[random.randint(0, 4)]}
    return JsonResponse(answer)
