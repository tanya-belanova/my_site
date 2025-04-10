from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def learn_words(request):
    return render(request, 'learn_words.html')

def add_words(request):
    return render(request, 'add_words.html')

def statistics(request):
    return render(request, 'statistics.html')

