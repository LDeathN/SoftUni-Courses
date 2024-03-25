# Generated by Django 5.0.2 on 2024-03-11 17:28

import CalisthenicsWorkoutTracker.workouts.validators
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('programs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3), CalisthenicsWorkoutTracker.workouts.validators.validate_workout_name], verbose_name='Workout Name')),
                ('difficulty', models.CharField(choices=[('Novice', 'Novice'), ('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced'), ('Mastery', 'Mastery')], max_length=15, verbose_name='Difficulty')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('duration', models.IntegerField(help_text='Minimum 30, Maximum 90', validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(90)], verbose_name='Duration (minutes)')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Image URL')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='programs.program', verbose_name='Program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
