from django.contrib import admin
from .extensions import (SeoExtension,
                         ThemeExtension)
from cms.extensions import PageExtensionAdmin
from .models import Theme

class PageExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(Theme)
admin.site.register(SeoExtension, PageExtensionAdmin)
admin.site.register(ThemeExtension, PageExtensionAdmin)
