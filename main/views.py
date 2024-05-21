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


def car_detail(request, slug):
    try:
        car = models.CarModels.objects.get(slug=slug)
        context = {
            'car': car,            
        }
    except models.CarModels.DoesNotExist:
        return render(request, '404.html')  

    return render(request, 'detail.html', context)

from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def log_in(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('front:index')
            else:
                return render(request,'login.html')
        except:
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':

        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            models.User.objects.create_user(
                username=username, 
                password=password, 
                first_name=f_name, 
                last_name=l_name
                )
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    return render(request, 'register.html')

def log_out(request):
    logout(request)
    return redirect('index')

# @login_required(login_url='login')
# def profile(request):

#     if request.method == 'POST':
#         username = request.user.username
#         f_name = request.POST.get('f_name')
#         l_name = request.POST.get('l_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         new_password = request.POST.get('new_password')
#         new_password_confirm = request.POST.get('new_password_confirm')
#         if authenticate(username=username,password=password):
#             user = models.User.objects.get(username=username)
#             user.first_name = f_name if f_name else ''
#             user.last_name = l_name if l_name else ''
#             user.email = email if email else ''
#             if new_password and new_password == new_password_confirm:
#                 user.set_password(new_password)
#             user.save()
#             return redirect('profile')
        
#     context = {'queryset':queryset}
#     return render(request, 'profile.html',context)

