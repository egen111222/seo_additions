from django.db import models

class File(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)

class Project(models.Model):
    name = models.CharField(max_length=150)
