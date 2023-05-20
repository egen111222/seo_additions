from django.utils.translation import gettext_lazy as _

def register_admin_menu(self,name,current_page_menu):
    page_extension, url = self.get_page_extension_admin()
    if url:
        current_page_menu.add_modal_item(_(name), url=url,
        disabled=not self.toolbar.edit_mode_active, position=0)


def global_populate(self,name):
    current_page_menu = self._setup_extension_toolbar()
    if current_page_menu:
        register_admin_menu(self,name,current_page_menu)
