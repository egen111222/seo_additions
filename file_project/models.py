from django.db import models
from seo.models import SeoAddition

class File(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    seo_addition = models.OneToOneField(
        SeoAddition,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=150)
    seo_addition = models.OneToOneField(
        SeoAddition,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return self.name
