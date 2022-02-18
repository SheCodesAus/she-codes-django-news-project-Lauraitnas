from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    url = models.URLField(max_length = 200, default="")
    category = models.ForeignKey('news.Category', related_name='stories', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()

    class Meta:
        ordering = ['-pub_date']

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name