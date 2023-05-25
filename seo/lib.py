def check_page_domain(page,domain):
    if (hasattr(page,"seoextension")
        and page.seoextension.domain_name.domain == domain):
        return True
    else:
        return False
    
