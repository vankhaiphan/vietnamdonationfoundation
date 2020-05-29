from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.urls import reverse

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

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("taochiendich"))
    else:
        return render(request, "vdf/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "vdf/login.html", {"message": "Logged out."})

def project_detail(request):
    return render(request, "vdf/project_detail.html")

def register(request):
    return render(request, "vdf/register.html")

def taochiendich(request):
    if not request.user.is_authenticated:
        return render(request, "vdf/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "vdf/taochiendich.html", context)

def donate(request):
    return render(request, "vdf/donate.html")
# def greet(request, name):
#     return render(request, "vdf/greet.html", {
#         "name":name.capitalize()
#     })