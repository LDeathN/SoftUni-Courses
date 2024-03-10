from django.db import models


class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.annotate(num_movies=models.Count('director_movies')).order_by('-num_movies', 'full_name')


class ActorManager(models.Manager):
    def get_top_actor(self):
        return self.annotate(num_of_movies=models.Count('movie')).order_by('-num_of_movies', 'full_name').first()