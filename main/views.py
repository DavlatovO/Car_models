from django.shortcuts import render
from . import models
def index(request):
    cars = models.CarModels.objects.all()
    categories = models.Category.objects.all()
    context = {
        'cars':cars,
        'categories':categories,
    }

    return render(request, 'index.html', context)