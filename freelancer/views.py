from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html")  # ✅ Pass request and template

def about(request):
    return render(request, "about.html")  # ✅ Just text for now

def contact(request):
    return render(request, "contact.html")  # ✅ Just text for now

def faq(request):
    return render(request, "faq.html")  # ✅ Just text for now

def services(request):
    return render(request, "services.html")  # ✅ Just text for now

def projects(request):
    return render(request, "projects.html")  # ✅ Just text for now

def blog(request):
    return render(request, "blog.html")  # ✅ Just text for now
