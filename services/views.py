from django.shortcuts import render , get_object_or_404
from .models import Options , Services , Features 


def post_detail(request , id):
    services = get_object_or_404(Services, id=id)
    options = Options.objects.all()
    features = Features.objects.all()

    context  = {
    "services" : services,
    "options" : options,
    "features" : features
    }

    return render(request , "services/service-details.html" , context=context)
