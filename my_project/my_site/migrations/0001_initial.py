# Generated by Django 5.2 on 2025-04-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spanish_word', models.CharField(max_length=100)),
                ('russian_translation', models.CharField(max_length=100)),
            ],
        ),
    ]
