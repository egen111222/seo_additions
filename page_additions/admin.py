from django.contrib import admin
from .extensions import (SeoKeyWordExtension,
                         ThemeExtension)
from cms.extensions import PageExtensionAdmin
from .models import Theme

class PageExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(Theme)
admin.site.register(SeoKeyWordExtension, PageExtensionAdmin)
admin.site.register(ThemeExtension, PageExtensionAdmin)
