from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=250)
    template = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DomainName(models.Model):
    domain_name = models.CharField(max_length=250)

    def __str__(self):
        return self.domain_name
