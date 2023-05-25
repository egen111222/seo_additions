from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from .libs import global_populate
from .extensions import (SeoExtension,
                         ThemeExtension)

@toolbar_pool.register
class SeoKeyWordExtensionToolbar(ExtensionToolbar):
    model = SeoExtension
    def populate(self):
        global_populate(self,"SEO EXTENSION")

@toolbar_pool.register
class ThemeExtensionToolbar(ExtensionToolbar):
    model = ThemeExtension
    def populate(self):
        global_populate(self,"PAGE THEME")
