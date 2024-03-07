from django.db import models
from django.core.validators import MinLengthValidator, ValidationError, MinValueValidator, EmailValidator, URLValidator
from decimal import Decimal

def validate_name(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError(f"Name can only contain letters and spaces")


def validate_phone_number(value):
    if value[0:4] != "+359" or not value[4:].isdigit():
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")


class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, message=ValidationError("Age must be greater than 18"))])
    email = models.EmailField(validators=[EmailValidator(message=ValidationError("Enter a valid email address"))])
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number])
    website_url = models.URLField(validators=[URLValidator(message=ValidationError('Enter a valid URL'))])


class BaseMedia(models.Model):
    class Meta:
        abstract = True
        ordering = ["-created_at", 'title']

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


class Book(BaseMedia):
    author = models.CharField(max_length=100, validators=[MinLengthValidator(5, message=ValidationError("Author must be at least 5 characters long"))])
    isbn = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(6, message=ValidationError("ISBN must be at least 6 characters long"))])

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Book"
        verbose_name_plural = "Models of type - Book"
        ordering = ["-created_at", 'title']


class Movie(BaseMedia):
    director = models.CharField(max_length=100, validators=[MinLengthValidator(8, message=ValidationError("Director must be at least 8 characters long"))])

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Movie"
        verbose_name_plural = "Models of type - Movie"
        ordering = ["-created_at", 'title']


class Music(BaseMedia):
    artist = models.CharField(max_length=100, validators=[MinLengthValidator(9, message=ValidationError("Artist must be at least 9 characters long"))])

    class Meta(BaseMedia.Meta):
        verbose_name = "Model Music"
        verbose_name_plural = "Models of type - Music"
        ordering = ["-created_at", 'title']


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_tax(self):
        return self.price * Decimal('0.08')

    def calculate_shipping_cost(self, weight):
        weight_decimal = Decimal(str(weight))
        return weight_decimal * Decimal('2.00')

    def format_product_name(self):
        return f"Product: {self.name}"

    def __str__(self):
        return self.name


class DiscountedProduct(Product):
    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        return self.price * Decimal('1.20')

    def calculate_tax(self):
        return self.price * Decimal('0.05')

    def calculate_shipping_cost(self, weight):
        weight_decimal = Decimal(str(weight))
        return weight_decimal * Decimal('1.50')

    def format_product_name(self):
        return f"Discounted Product: {self.name}"

    def __str__(self):
        return f"Discounted {super().__str__()}"


class RechargeEnergyMixin(models.Model):
    def recharge_energy(self, amount):
        self.energy += amount
        self.energy = min(self.energy, 100)
        self.save()

    class Meta:
        abstract = True


class Hero(RechargeEnergyMixin, models.Model):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)
    energy = models.PositiveIntegerField()


class SpiderHero(Hero):
    class Meta:
        proxy = True

    def swing_from_buildings(self):
        if self.energy - 80 <= 0:
            return f"{self.name} as Spider Hero is out of web shooter fluid"
        else:
            self.energy -= 80
            self.save()
            return f"{self.name} as Spider Hero swings from buildings using web shooters"


class FlashHero(Hero):
    class Meta:
        proxy = True

    def run_at_super_speed(self):
        if self.energy - 65 <= 0:
            return f"{self.name} as Flash Hero needs to recharge the speed force"
        else:
            self.energy -= 65
            self.save()
            return f"{self.name} as Flash Hero runs at lightning speed, saving the day"



