from django.db import models


class ProfileManager(models.Manager):
    def get_regular_customers(self):
        return self.annotate(num_of_orders=models.Count('orders')).filter(num_of_orders__gt=2).order_by('-num_of_orders')

