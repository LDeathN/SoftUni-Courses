import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Review, Author, Article
from django.db.models import Q, F, Count, Avg


def get_authors(search_name=None, search_email=None):
    if search_name is None and search_email is None:
        return ""

    query = Q()
    query_names = Q(full_name__icontains=search_name)
    query_emails = Q(email__icontains=search_email)

    if search_name and search_email:
        query |= query_emails & query_names
    elif search_name:
        query |= query_names
    else:
        query |= query_emails

    authors = Author.objects.filter(query).order_by('-full_name')

    if not authors:
        return ""

    result = []
    [result.append(f"Author: {a.full_name}, email: {a.email}, status: {'Banned' if a.is_banned else 'Not Banned'}") for a in authors]

    return "\n".join(result)


def get_top_publisher():
    author = Author.objects.get_authors_by_article_count().first()
    if not author or author.article_count == 0:
        return ""
    return f"Top Author: {author.full_name} with {author.article_count} published articles."


def get_top_reviewer():
    author = Author.objects.annotate(review_count=Count('reviews')).order_by('-review_count', 'email').first()
    if not author or author.review_count == 0:
        return ""
    return f"Top Reviewer: {author.full_name} with {author.review_count} published reviews."


def get_latest_article():
    article = Article.objects.prefetch_related('authors', 'reviews').order_by('-published_on').first()
    if not article:
        return ""

    authors_names = ', '.join(author.full_name for author in article.authors.all().order_by('full_name'))
    num_reviews = article.reviews.count()
    avg_rating = sum([r.rating for r in article.reviews.all()]) / num_reviews if num_reviews else 0.0

    return f"The latest article is: {article.title}. Authors: {authors_names}. Reviewed: {num_reviews} times. Average Rating: {avg_rating:.2f}."


def get_top_rated_article():
    top_rated_article = Article.objects.annotate(avg_rating=Avg('reviews__rating')).order_by('-avg_rating', 'title').first()
    num_reviews = top_rated_article.reviews.count() if top_rated_article else 0
    if top_rated_article is None or num_reviews == 0:
        return ''

    avg_rating = top_rated_article.avg_rating or 0.0
    return f"The top-rated article is: {top_rated_article.title}, with an average rating of {avg_rating:.2f}, reviewed {num_reviews} times."


def ban_author(email=None):
    author = Author.objects.prefetch_related('reviews').filter(email__exact=email).first()
    if email is None or author is None:
        return "No authors banned."

    num_reviews_deleted = author.reviews.count()

    author.is_banned = True
    author.save()
    author.reviews.all().delete()

    return f"Author: {author.full_name} is banned! {num_reviews_deleted} reviews deleted."



