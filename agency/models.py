from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField()
    REQUIRED_FIELDS = ['years_of_experience', ]

    class Meta:
        ordering = ["username"]


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()
    published_date = models.DateField(auto_now=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} {self.context} ({self.published_date})"
