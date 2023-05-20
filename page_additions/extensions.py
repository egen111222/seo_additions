from .models import Theme
from seo.models import SeoKeyWord
from seo.models import DomainName
from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

class ThemeExtension(PageExtension):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)    

class SeoKeyWordExtension(PageExtension):
    keywords = models.ManyToManyField(SeoKeyWord)
    domain_name = models.ForeignKey(DomainName, on_delete=models.CASCADE)


extension_pool.register(ThemeExtension)
extension_pool.register(SeoKeyWordExtension)
