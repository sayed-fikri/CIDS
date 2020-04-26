from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Annoucement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


