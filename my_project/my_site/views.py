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
                word_cards = list(WordCard.objects.all())
                random_words = random.sample(word_cards, min(num_words, len(word_cards)))
                return render(request, 'learn_words.html', {'word_cards': random_words})
        elif any(key.startswith('translation_') for key in request.POST.keys()):
            word_cards = WordCard.objects.all()
            translations = {}
            for word in word_cards:
                translation = request.POST.get(f'translation_{word.id}')
                translations[word.id] = translation

            results = []
            for word in word_cards:
                if f'translation_{word.id}' in request.POST:
                    correct_translation = word.russian_translation
                    user_translation = translations[word.id]
                    if user_translation.lower() == correct_translation.lower():
                        results.append({
                            'word': word.spanish_word,
                            'correct': True,
                            'user_translation': user_translation,
                            'correct_translation': correct_translation
                        })
                    else:
                        results.append({
                            'word': word.spanish_word,
                            'correct': False,
                            'user_translation': user_translation,
                            'correct_translation': correct_translation
                        })

            return render(request, 'results.html', {
                'results': results
            })
        else:
            # Обработка случая, когда запрос не содержит 'num_words' и 'translation_'
            return render(request, 'learn_words.html', {'error': 'Неправильный запрос'})
    else:
        form = LearnWordsForm()
        return render(request, 'learn_words.html', {'form': form})
