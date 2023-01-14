from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(blank=False)
    REQUIRED_FIELDS = ["years_of_experience", ]

    class Meta:
        ordering = ["username"]
        verbose_name = "redactor"
        verbose_name_plural = "redactors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("agency:redactor-detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255, unique=True)
    context = models.TextField(blank=False)
    published_date = models.DateField(auto_now=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} {self.context} ({self.published_date})"

    def get_absolute_url(self):
        return reverse("agency:newspaper-detail", kwargs={"pk": self.pk})
