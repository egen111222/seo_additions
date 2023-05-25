from cms.models import Page
from .lib import check_page_domain
from .models import DomainName
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap


class SiteMapService:
    def get_domain_pages(self,domain):
        pages = Page.objects.all()
        page_ids = [page.id for page in pages if check_page_domain(page,domain)]
        return Page.objects.filter(id__in=page_ids)
    # ................ get_domain_projects

    
