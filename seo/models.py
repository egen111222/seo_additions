from django.db import models

class SeoKeyWord(models.Model):
    keyword = models.CharField(max_length=150)

    def __str__(self):
        return self.tag

class SeoAddition(models.Model):
    element = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    keywords = models.ManyToManyField(SeoKeyWord)

    def __str__(self):
        return self.element
