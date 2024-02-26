from django.db import migrations

def item_rarity(apps, schema_editor):
    Item = apps.get_model('main_app', "Item")
    all_items = Item.objects.all()
    for i in range(len(all_items)):
        item = all_items[i]
        if item.price <= 10:
            item.rarity = "Rare"
        elif 11 <= item.price <= 20:
            item.rarity = "Very Rare"
        elif 21 <= item.price <= 30:
            item.rarity = "Extremely Rare"
        elif item.price >= 31:
            item.rarity = "Mega Rare"
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_item'),
    ]

    operations = [
    ]
