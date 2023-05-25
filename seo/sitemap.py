from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from .lib import check_page_domain
from .models import DomainName
from .services import SiteMapService


sitemap_service = SiteMapService()

def set_sitemaps():
    domains = DomainName.objects.all()
    sitemaps = {}
    for domain in domains:
        domain_obejct = GenericSitemap({"queryset":sitemap_service.get_domain_pages(domain.domain)},1)
        sitemaps.setdefault(f"{domain.domain}_sitemap.xml",{"sitemaps":{f"{domain.domain}":domain_obejct}})
    return sitemaps

sitemaps = set_sitemaps()
