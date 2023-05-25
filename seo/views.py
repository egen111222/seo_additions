from django.shortcuts import render
from .services import SiteMapService
from django.http import HttpResponse

sitemap_service = SiteMapService()

def get_sitemaps(request,domain):
    pages = sitemap_service.get_domain_pages(domain)
    return render(request,
                  "page_sitemap.html",
                  context={"pages":pages,
                           "domain":domain},
                  content_type="application/xhtml+xml")
    
