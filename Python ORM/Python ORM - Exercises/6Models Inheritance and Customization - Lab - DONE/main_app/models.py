from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True


class ZooKeeper(Employee):
    SPECIALITIES = [
        ("Mammals", "Mammals"),
        ("Birds", "Birds"),
        ("Reptiles", "Reptiles"),
        ("Others", "Others"),
    ]
    specialty = models.CharField(max_length=10, choices=SPECIALITIES)
    managed_animals = models.ManyToManyField("Animal")

    def clean(self):
        super().clean()

        if self.specialty not in dict(self.SPECIALITIES).keys():
            raise ValidationError("Specialty must be a valid choice.")


class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = ((True, 'Available'),
                             (False, 'Not Available'))

        kwargs['default'] = True
        super().__init__(*args, **kwargs)


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10,)
    availability = BooleanChoiceField()

    def is_available(self):
        return self.availability


class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

    def display_info(self):
        extra_info = ""
        if hasattr(self, "mammal"):
            extra_info = f" Its fur color is {self.mammal.fur_color}."
        elif hasattr(self, "bird"):
            extra_info = f" Its wingspan is {self.bird.wing_span} cm."
        elif hasattr(self, "reptile"):
            extra_info = f" Its scale type is {self.reptile.scale_type}."
        return f"Meet {self.name}! It's {self.species} and it's born {self.birth_date}. It makes a noise like '{self.sound}'!{extra_info}"

    def is_endangered(self):
        endangered_species = ["Cross River Gorilla", "Orangutan", "Green Turtle"]
        return self.species in endangered_species


