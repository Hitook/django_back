# Generated by Django 4.1.1 on 2022-10-04 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_trivia_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='trivia',
            name='average_score',
            field=models.IntegerField(default=0),
        ),
    ]