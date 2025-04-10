from django.shortcuts import render, redirect
from .models import WordCard
from .forms import WordForm, LearnWordsForm
from django.db.models import Q
import random

def index(request):
    return render(request, 'index.html')


def add_words(request):
    if request.method == 'POST':
        if 'add_word' in request.POST:
            form = WordForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('add_words')
        elif 'delete_word' in request.POST:
            word_id = request.POST.get('delete_word')
            WordCard.objects.filter(id=word_id).delete()
            return redirect('add_words')
    
    form = WordForm()
    word_cards = WordCard.objects.all()
    
    return render(request, 'add_words.html', {'form': form, 'word_cards': word_cards})

def learn_words(request):
    if request.method == 'POST':
        form = LearnWordsForm(request.POST)
        if form.is_valid():
            num_words = form.cleaned_data['num_words']
            word_cards = list(WordCard.objects.all())
            random_words = random.sample(word_cards, min(num_words, len(word_cards)))
            return render(request, 'learn_words.html', {'word_cards': random_words})
    else:
        form = LearnWordsForm()
    
    return render(request, 'learn_words.html', {'form': form})

def statistics(request):
    return render(request, 'statistics.html')