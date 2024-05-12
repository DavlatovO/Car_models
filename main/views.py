from django.shortcuts import render
from . import models
def index(request):
    cars = models.CarModels.objects.all()
    categories = models.Category.objects.all()
    last = models.CarModels.objects.order_by('-id')[:3]
    context = {
        'cars':cars,
        'categories':categories,
        'last':last
    }

    return render(request, 'index.html', context)

def contact(request):

    return render(request, 'contact.html')
