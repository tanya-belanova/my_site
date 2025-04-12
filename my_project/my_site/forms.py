from django import forms
from .models import WordCard

class WordForm(forms.ModelForm):
    class Meta:
        model = WordCard
        fields = ('spanish_word', 'russian_translation')

class LearnWordsForm(forms.Form):
    num_words = forms.IntegerField(
        min_value=1,
        label = '',
        error_messages={
            'required': 'Поле не должно быть пустым!',
            'min_value': 'Значение не должно быть меньше 1'
        },
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control rounded-3'
            }
        )
        
    )

class TranslationForm(forms.Form):
    def __init__(self, word_cards, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for word in word_cards:
            self.fields[f'translation_{word.id}'] = forms.CharField(
                label=f'Перевод для "{word.spanish_word}"',
                required=True
            )