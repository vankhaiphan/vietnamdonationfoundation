from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "vdf/index.html", { "user": request.user.username} )
    return render(request, "vdf/index.html", { "user" : ""})

def about(request):
    return render(request, "vdf/about.html")

def articles(request):
    return render(request, "vdf/articles.html")

def explore_pages(request):
    return render(request, "vdf/explore_pages.html")

def explore_result(request):
    return render(request, "vdf/explore_result.html")

def thankyou(request):
    return render(request, "vdf/thankyou.html")
def explore(request):
    if request.user.is_authenticated:
        return render(request, "vdf/explore.html", { "user": request.user.username} )
    return render(request, "vdf/explore.html", { "user": ""})

def login_view(request):
    username = request.POST.get('username', '') #get username, if there's none, set default ''
    password = request.POST.get('password', '') #get password, if there's none, set default ''
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

def resetpassword(request):
    return render(request, "vdf/resetpassword.html")

def taochiendich(request):
    if not request.user.is_authenticated:
        return render(request, "vdf/login.html", {"message": None})
    context = {
        "user": request.user.username
    }
    return render(request, "vdf/taochiendich.html", context)

def donate(request):
    return render(request, "vdf/donate.html")
# def greet(request, name):
#     return render(request, "vdf/greet.html", {
#         "name":name.capitalize()
#     })
def AdminCampaign(request):
    return render(request, "vdf/AdminCampaign.html")

def AdminShowUser(request):
    return render(request, "vdf/AdminShowUser.html")

def AdminUserEdit(request):
    return render(request, "vdf/AdminUserEdit.html")
    
def AdminChangePassword(request):
    return render(request, "vdf/AdminChangePassword.html")

def supAdminshowUsers(request):
    return render(request,"vdf/supAdminshowUsers.html")

def supAdminShowDetails(request):
    return render(request,"vdf/supAdminShowDetails.html")

def supAdminEdit(request):
    return render(request,"vdf/supAdminEdit.html")

def supAdminCampaign(request):
    return render(request, "vdf/supAdminCampaign.html")

def supAdminadduser(request):
    return render(request,"vdf/supAdminadduser.html")

def Feedback(request):
    return render(request,"vdf/Feedback.html")