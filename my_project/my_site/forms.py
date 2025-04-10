from django import forms
from .models import WordCard

class WordForm(forms.ModelForm):
    class Meta:
        model = WordCard
        fields = ('spanish_word', 'russian_translation')

class LearnWordsForm(forms.Form):
    num_words = forms.IntegerField(min_value=1, label='Количество слов для изучения')