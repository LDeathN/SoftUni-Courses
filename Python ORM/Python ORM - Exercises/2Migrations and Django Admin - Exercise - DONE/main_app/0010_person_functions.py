from django.db import migrations
from django.utils import timezone


def add_age_group(apps, schema_editor):
    Person = apps.get_model('main_app', 'Person')
    all_people = Person.objects.all()
    for i in range(len(all_people)):
        person = all_people[i]
        if person.age <= 12:
            person.age_group = 'Child'
        elif 13 <= person.age <= 17:
            person.age_group = "Teen"
        else:
            person.age_group = "Adult"
        person.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_person'),
    ]

    operations = [migrations.RunPython(add_age_group)
    ]
