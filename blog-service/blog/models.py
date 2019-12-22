from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    comment_to = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    author_id = models.CharField(max_length=250)
