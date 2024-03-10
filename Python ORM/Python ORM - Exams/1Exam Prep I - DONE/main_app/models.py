from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator
from main_app.managers import DirectorManager, ActorManager


class Director(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default="Unknown")
    years_of_experience = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])

    objects = DirectorManager()


class Actor(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default="Unknown")
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)

    objects = ActorManager()


class Movie(models.Model):
    title = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)
    GENRES = [
        ("Action", "Action"),
        ("Comedy", "Comedy"),
        ("Drama", "Drama"),
        ("Other", "Other"),
    ]
    genre = models.CharField(choices=GENRES, default="Other", max_length=6)
    rating = models.DecimalField(default=0.0, max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    is_classic = models.BooleanField(default=False)
    is_awarded = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True)
    director = models.ForeignKey(to=Director, on_delete=models.CASCADE, related_name='director_movies')
    starring_actor = models.ForeignKey(to=Actor, on_delete=models.SET_NULL, null=True, related_name='starring_movies',)
    actors = models.ManyToManyField(Actor, related_name='actor_movies',)


