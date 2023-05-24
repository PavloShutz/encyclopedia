from django.db import models


class SavedArticle(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    content = models.TextField(null=False)
