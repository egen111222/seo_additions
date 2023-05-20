from .models import Theme
from seo.models import SeoKeyWord
from django.db import models
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

class ThemeExtension(PageExtension):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)    

class SeoKeyWordExtension(PageExtension):
    keywords = models.ManyToManyField(SeoKeyWord)
    

extension_pool.register(ThemeExtension)
extension_pool.register(SeoKeyWordExtension)
