from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    

def admin(request):
    return render(request,'index-3.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')

def main(request):
    return render(request,'index-2.html')


def about(request):
    return render(request,'about-us.html')

def service(request):
    return render(request,'service.html')

def blog(request):
    return render(request,'blog-details.html')

def contact(request):
    return render(request,"contact.html")
