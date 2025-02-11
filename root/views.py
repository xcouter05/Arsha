from django.shortcuts import render
from services.models import Services
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    services = Services.objects.filter(status = True ).order_by("id")  

    #search 
    if request.GET.get('search'):
        search = request.GET.get('search', '').strip()  # حذف فاصله‌های اضافی
        services = Services.objects.filter(
            status=True
        ).filter(
            Q(title__icontains=search) |  # جستجو در `title`
            Q(desc__icontains=search) |    # جستجو در `desc`
            Q(content__icontains=search)   # جستجو در `content`
        )[:6]  
    else:
        services = Services.objects.filter(status=True)[:6]  


    #paginator 
    services_paginate = Paginator(services, 3)  
    page_number = request.GET.get("page", 1)  
    services = services_paginate.get_page(page_number) 

    context = {
        "services": services,
        "first": 1,
        "last": services.paginator.num_pages,
    }

    return render(request, "root/index.html", context=context)
