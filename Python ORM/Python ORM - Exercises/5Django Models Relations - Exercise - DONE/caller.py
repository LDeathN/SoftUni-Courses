import os
import django
from datetime import timedelta, date
# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book
from main_app.models import Artist, Song
from main_app.models import Product, Review
from main_app.models import Driver, DrivingLicense
from main_app.models import Car, Registration, Owner

#First
def show_all_authors_with_their_books():
    result = []
    authors = Author.objects.all()
    for author in authors:
        books = Book.objects.filter(author=author)
        if books:
            books = sorted(books, key=lambda book: book.id)
            result.append(f"{author.name} has written - {', '.join(str(book.title) for book in books)}!")
    return "\n".join(result)

def delete_all_authors_without_books():
    authors = Author.objects.all()
    for author in authors:
        books = Book.objects.filter(author=author)
        if not books:
            author.delete()


#Second
def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)

def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    songs = artist.songs.all().order_by('-id')
    return songs

def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


#Third
def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = Review.objects.filter(product=product)
    total_rating = sum(review.rating for review in reviews)
    average_rating = total_rating / len(reviews)
    return average_rating

def get_reviews_with_high_ratings(threshold: int):
    high_rating_reviews = Review.objects.filter(rating__gte=threshold)
    return high_rating_reviews

def get_products_with_no_reviews():
    products_with_no_reviews = Product.objects.filter(reviews__isnull=True).order_by('-name')
    return products_with_no_reviews

def delete_products_without_reviews():
    get_products_with_no_reviews().delete()

# Fourth
def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.order_by('-license_number')
    return '\n'.join(str(l) for l in licenses)

def get_drivers_with_expired_licenses(due_date):
    date = due_date - timedelta(days=365)
    expired_drivers = Driver.objects.filter(drivinglicense__issue_date__gt=date)
    return expired_drivers


#Fifth
def register_car_by_owner(owner: object):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True, owner=owner).first()

    car.owner = owner
    car.registration = registration
    car.save()

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."
