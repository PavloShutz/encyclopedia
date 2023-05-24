"""Database services."""

from django.db.utils import IntegrityError

from .models import SavedArticle


def save_article(word: str, content: str):
    """Save article's name and content into db."""
    try:
        article = SavedArticle(name=word, content=content)
        article.save()
    except IntegrityError:
        pass
