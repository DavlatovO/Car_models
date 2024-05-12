from django.core.mail import send_mail
from django.shortcuts import render, redirect
from . import models
from datetime import datetime


def index(request):
    cars = models.CarModels.objects.all()
    categories = models.Category.objects.all()
    contacts = models.Contact.objects.exclude(email='davlaek@gmail.com')
    last = models.CarModels.objects.order_by('-id')[:3]
    context = {
        'cars':cars,
        'categories':categories,
        'last':last,
        'contacts':contacts
    }

    return render(request, 'index.html', context)
 
def contact(request):
    if request.method == 'POST':
        try:
            models.Contact.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message']
            )
        except:
            ...
    return render(request, 'contact.html')

