from django.db import models

class SeoKeyWord(models.Model):
    keyword = models.CharField(max_length=150)

    def __str__(self):
        return self.keyword
    
class DomainName(models.Model):
    domain = models.CharField(max_length=50)
    # one To One на GoogleTag
    def __str__(self):
        return self.domain

class SeoAddition(models.Model):
    element = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    keywords = models.ManyToManyField(SeoKeyWord)
    # domain через ForeignKey на DomainName м получаем domain и получаем google tag отслежитвания
    def __str__(self):
        return self.element

class GoogleTag(models.Model):
    script = models.TextField()
