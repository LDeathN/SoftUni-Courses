from django.db import migrations


def create_price(apps, schema_editor):
    Smartphone = apps.get_model('main_app', "Smartphone")
    all_phones = Smartphone.objects.all()
    for i in range(len(all_phones)):
        smartphone = all_phones[i]
        smartphone.price = len(smartphone.brand) * 120
        smartphone.save()


def get_category(apps, schema_editor):
    Smartphone = apps.get_model('main_app', "Smartphone")
    all_phones = Smartphone.objects.all()
    for i in range(len(all_phones)):
        smartphone = all_phones[i]
        if smartphone.price >= 750:
            smartphone.category = "Expensive"
        else:
            smartphone.category = "Cheap"
        smartphone.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_smartphone'),
    ]

    operations = [
    ]
