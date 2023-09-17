from django.urls import path
from . import views



urlpatterns = [
    path('',views.main,name="main"),
    path('main', views.main, name='main'),
    path('loginpage', views.index, name='login'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    ]