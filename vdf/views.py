from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.urls import reverse
from django.db import models
from .models import Campaign


# Create your views here.
def index(request):
    return checkAuthenticationThenRedirect(request, "vdf/index.html")


def about(request):
    return checkAuthenticationThenRedirect(request, "vdf/about.html")


def articles(request):
    return checkAuthenticationThenRedirect(request, "vdf/articles.html")


def explore_pages(request):
    return checkAuthenticationThenRedirect(request, "vdf/explore_pages.html")


def explore_result(request):
    return checkAuthenticationThenRedirect(request, "vdf/explore_result.html")


def thankyou(request):
    return checkAuthenticationThenRedirect(request, "vdf/thankyou.html")


def explore(request):
    return checkAuthenticationThenRedirect(request, "vdf/explore.html")


def faq(request):
    return checkAuthenticationThenRedirect(request, "vdf/faq.html")

def faqs(request):
    return checkAuthenticationThenRedirect(request, "vdf/faqs.html")


def resetpassword(request):
    return checkAuthenticationThenRedirect(request, "vdf/resetpassword.html")        


def login_view(request):
    username = request.POST.get('username', '') #get username, if there's none, set default ''
    password = request.POST.get('password', '') #get password, if there's none, set default ''
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("taochiendich"))
    else:
        return render(request, "vdf/login.html", {"message": "Invalid credentials.", "user": ""})


def logout_view(request):
    logout(request)
    return render(request, "vdf/login.html", {"message": "Logged out.", "user": ""})


def project_detail(request):
    return checkAuthenticationThenRedirect(request, "vdf/project_detail.html")


def register(request):
    return checkAuthenticationThenRedirect(request, "vdf/register.html")


def taochiendich(request):
    if not request.user.is_authenticated:
        return render(request, "vdf/login.html", {"user": ""})
    return render(request, "vdf/taochiendich.html", { "user": request.user.username})


def donate(request):
    return checkAuthenticationThenRedirect(request, "vdf/donate.html")
# def greet(request, name):
#     return render(request, "vdf/greet.html", {
#         "name":name.capitalize()
#     })


def AdminCampaign(request):
    return checkAuthenticationThenRedirect(request, "vdf/AdminCampaign.html")


def AdminShowUser(request):
    return checkAuthenticationThenRedirect(request, "vdf/AdminShowUser.html")


def AdminUserEdit(request):
    return checkAuthenticationThenRedirect(request, "vdf/AdminUserEdit.html")


def AdminChangePassword(request):
    return checkAuthenticationThenRedirect(request, "vdf/AdminChangePassword.html")


def supAdminshowUsers(request):
    return checkAuthenticationThenRedirect(request, "vdf/supAdminshowUsers.html")


def supAdminShowDetails(request):
    return checkAuthenticationThenRedirect(request, "vdf/supAdminShowDetails.html")


def supAdminEdit(request):
    return checkAuthenticationThenRedirect(request, "vdf/supAdminEdit.html")


def supAdminCampaign(request):
    all_Cams = Campaign.object.all()
    #return checkAuthenticationThenRedirect(request, "vdf/supAdminCampaign.html", {'Campaigns': all_Cams})
    return render(request, "vdf/supAdminCampaign.html", {'Campaigns': all_Cams})



def supAdminadduser(request):
    return checkAuthenticationThenRedirect(request, "vdf/supAdminadduser.html")


def Feedback(request):
    return checkAuthenticationThenRedirect(request, "vdf/Feedback.html")

def contact(request):
    return checkAuthenticationThenRedirect(request, "vdf/contact.html")

def checkAuthenticationThenRedirect(request, page_name):
    if request.user.is_authenticated:
        return render(request, page_name, { "user": request.user.username})
    
    return render(request, page_name, { "user": ""})

# def queryCampaign(request):
#     all_Cams = Campaign.object.all()
#     return render(request, "vdf/supAdminCampaign.html", {'Campaigns': all_Cams})
