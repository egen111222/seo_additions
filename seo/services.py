from cms.models import Page

class SiteMapPageService:
    def get_doamin_pages(self,domain):
        return Page.objects\
                      .\filter(seokeywordextension is not None)\
                      .filter(seokeywordextension.damoin_name == domain)\
                      all()
