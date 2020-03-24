# Generated by Django 3.0.3 on 2020-02-22 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_userinputquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MCQ', 'Multiple Choice Question'), ('TFQ', 'True False Question'), ('UIQ', 'User Input Question')], default='MCQ', max_length=3),
        ),
    ]
