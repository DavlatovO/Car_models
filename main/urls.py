from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('car-detail/<slug:slug>/', views.car_detail, name='car_detail'),
    path('login/',views.log_in,name='login'),
    path('logout/',views.log_out,name='logout'),
    path('register/',views.register,name='register'),
    # path('profile/',views.profile,name='profile'),

]