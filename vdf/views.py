from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "vdf/index.html")

def about(request):
    return render(request, "vdf/about.html")

def articles(request):
    return render(request, "vdf/articles.html")

def explore_pages(request):
    return render(request, "vdf/explore_pages.html")

def explore_result(request):
    return render(request, "vdf/explore_result.html")

def explore(request):
    return render(request, "vdf/explore.html")

def login(request):
    return render(request, "vdf/login.html")

def project_detail(request):
    return render(request, "vdf/project_detail.html")

def register(request):
    return render(request, "vdf/register.html")

def taochiendich(request):
    return render(request, "vdf/taochiendich.html")


# def greet(request, name):
#     return render(request, "vdf/greet.html", {
#         "name":name.capitalize()
#     })