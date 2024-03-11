import os
import django
from django.db.models import Q, Count, Avg, F, Subquery, OuterRef

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Profile, Product, Order


def get_profiles(search_string=None):
    result = []
    if search_string is not None:
        profiles = Profile.objects \
            .annotate(num_orders=Count('orders')) \
            .filter(Q(full_name__icontains=search_string)
                    | Q(email__icontains=search_string)
                    | Q(phone_number__icontains=search_string)) \
            .order_by('full_name')

        [result.append(f'Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, '
                       f'orders: {p.num_orders}') for p in profiles]

    return '\n'.join(result) if result else ''


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()
    if not profiles:
        return ""

    result = []
    [result.append(f"Profile: {profile.full_name}, orders: {profile.num_of_orders}") for profile in profiles]

    return "\n".join(result)


def get_last_sold_products():
    last_order = Order.objects.last()

    if not last_order:
        return ""

    products = last_order.products.all().order_by('name')
    if not products:
        return ""

    result = f"Last sold products: {', '.join([product.name for product in products])}"
    return result


def get_top_products():
    products = Product.objects.annotate(num_orders=Count('orders')).filter(num_orders__gt=0).order_by('-num_orders', 'name')[:5]

    if not products or not products[0].num_orders:
        return ""

    result = ["Top products:"]
    for product in products:
        result.append(f"{product.name}, sold {product.num_orders} times")

    return "\n".join(result)


def apply_discounts():
    orders = Order.objects.annotate(num_of_products=Count('products')).filter(num_of_products__gt=2, is_completed=False)
    if not orders:
        num_of_updated_orders = 0
    else:
        num_of_updated_orders = orders.update(total_price=F('total_price') * 0.90)

    return f"Discount applied to {num_of_updated_orders} orders."


def complete_order():
    order = Order.objects.filter(is_completed=False).order_by('creation_date').first()
    if order is None:
        return ""

    order.is_completed = True
    order.save()

    for product in order.products.all():
        product.in_stock -= 1

        if product.in_stock == 0:
            product.is_available = False
        product.save()

    return "Order has been completed!"


