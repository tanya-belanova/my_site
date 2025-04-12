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
        if 'num_words' in request.POST:
            form = LearnWordsForm(request.POST)
            if form.is_valid():
                num_words = form.cleaned_data['num_words']
                all_words = list(WordCard.objects.all())
                
                num_words = min(num_words, len(all_words))
                
                if num_words < 1:
                    form.add_error('num_words', 'Число должно быть не менее 1')
                    return render(request, 'learn_words.html', {'form': form})
                
                random_words = random.sample(all_words, num_words)
                return render(request, 'learn_words.html', {'word_cards': random_words})
            
            return render(request, 'learn_words.html', {'form': form})

        elif any(key.startswith('translation_') for key in request.POST):
            results = []
            for key, value in request.POST.items():
                if key.startswith('translation_'):
                    word_id = key.split('_')[1]
                    try:
                        word = WordCard.objects.get(id=word_id)
                        user_translation = value.strip().lower()
                        correct = user_translation == word.russian_translation.lower()
                        results.append({
                            'word': word.spanish_word,
                            'correct': correct,
                            'user_translation': value,
                            'correct_translation': word.russian_translation
                        })
                    except WordCard.DoesNotExist:
                        continue
            
            return render(request, 'results.html', {'results': results})
        
        return render(request, 'learn_words.html', {'form': LearnWordsForm()})

    form = LearnWordsForm()
    return render(request, 'learn_words.html', {'form': form})
