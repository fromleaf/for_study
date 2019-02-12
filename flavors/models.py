from django.urls import reverse
from django.db import models


class Flavor(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    scoops_remaining = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("flavors:detail", kwargs={"slug": self.slug})
