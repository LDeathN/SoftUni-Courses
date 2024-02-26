from django.db import migrations


def delivery_setter(apps, schema_editor):
    Order = apps.get_model('main_app', "Order")
    all_orders = Order.objects.all()
    for i in range(len(all_orders)):
        order = all_orders[i]
        if order.status == "Pending":
            order.delivery = order.order_date + 3
        elif order.status == "Completed":
            order.warranty = "24 months"
        elif order.status == "Cancelled":
            order.delete()
        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_order'),
    ]

    operations = [
    ]
