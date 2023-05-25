from django.db import models


class SavedArticle(models.Model):
    """Table in database for saving every new article user has found."""
    name = models.CharField(max_length=200, null=False, unique=True)
    content = models.TextField(null=False)
