from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    bio = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse("get-profile", kwargs={"pk": self.pk})