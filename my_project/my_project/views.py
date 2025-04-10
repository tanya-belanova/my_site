from django.shortcuts import render
from .models import WordCard


def index(request):
    return render(request, 'index.html')

def learn_words(request):
    word_cards = WordCard.objects.all()
    return render(request, 'learn_words.html', {'word_cards': word_cards})

def add_words(request):
    return render(request, 'add_words.html')

def statistics(request):
    return render(request, 'statistics.html')