from django.db import models

class WordCard(models.Model):
    spanish_word = models.CharField(max_length=100)
    russian_translation = models.CharField(max_length=100)

    class Meta:
        app_label = 'my_project'

    def __str__(self):
        return self.spanish_word