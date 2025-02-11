from django.shortcuts import render
from services.models import Services
def home(request):
    services = Services.objects.all()
    context = {
        "services": services
    }
    return render(request, "root/index.html" , context=context)

