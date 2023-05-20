from django.shortcuts import render
from cms.models import Page

def get_all_pages(request):
    pages = Page.objects.all()
    return render(request,"seo_test.html",context={"pages":pages})
    
