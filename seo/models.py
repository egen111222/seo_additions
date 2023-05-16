from django.db import models

class SeoAddition(models.Model):
    element = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class SeoTag(models.Model):
    tag = models.CharField(max_length=150)

    def __str__(self):
        return self.tag


