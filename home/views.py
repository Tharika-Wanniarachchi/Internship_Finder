from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import Company
from .form import AddCompany


# Create your views here.


def home(request):
    database = Company.objects.all()
    return render(request, "home/index.html", context={'page':'Find i web Application','database':database})


def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html",context)

def category(request):
    context = {'page': 'category'}
    return render(request, "home/category.html", context)

# def company(request, pid):
#     company_info = Company.objects.get(id=pid)
#     context = {
#         'page': 'company',
#         'company': company_info,  # Pass the company information to the template
#         'logo_url': company_info.image.url # Pass the URL of the company's image
#     }
#     return render(request, "home/company.html", context=context)

def company(request, pid):
    company_info = Company.objects.get(id=pid)
    context = {
        'page': 'company',
        'company': company_info,  # Pass the company information to the template
    }
    return render(request, "home/company.html", context)

def registration(request):
    if request.method == "POST":
        form = AddCompany(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddCompany()
    return render(request, "home/registration.html", {'form': form})

def updateRegistration(request,pid):
    company_info = Company.objects.get(id=pid)
    form =AddCompany(instance=company_info)
    if request.method == "POST":
        form = AddCompany(request.POST, request.FILES, instance=company_info) 
        if form.is_valid():
            form.save()
            return redirect('home') 
    return render(request,'home/registration.html',{'form':form})

def deleteRegistration(request,pid) :
    company_info = Company.objects.get(id=pid)
    if request.method == "POST":
        company_info.delete()
        return redirect('home')
    return render(request,'home/delete.html')


def login(request):
    context = {'page': 'login'}
    return render(request, "home/login.html",context)

def forget_password(request):
    context = {'page': 'forget_password'}
    return render(request, "home/forget_password.html",context)

def vacancy(request):
    context = {'page': 'vacancy'}
    return render(request, "home/vacancy.html",context)

def success_page(request):
    return HttpResponse("<h1>Hey This is a Succes page.</h1>")

def contact(request):
    context = {'page': 'contact'}
    return render(request, "home/contact.html",context)
