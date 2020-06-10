from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AddCampaignForm
from .models import UserDetail, Campaign, Donation
from django.views.generic import TemplateView, ListView


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
    return checkAuthenticationThenRedirect(request, "vdf/taochiendich.html")


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
    return checkAuthenticationThenRedirect(request, "vdf/supAdminCampaign.html")


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

def AddCampaignProcess(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = AddCampaignForm(request.POST, request.FILES)
        #print(request.FILES['coverImage'])     
        print(request.POST)
        print(request.FILES)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            print("is valid")
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            shortDescription = form.cleaned_data['shortDescription']
            goal = form.cleaned_data['goal']
            fullDescription = form.cleaned_data['fullDescription']
            expiredDate = form.cleaned_data['expiredDate']
            coverImage = form.cleaned_data['coverImage']
            ownerID = UserDetail.objects.get(id=request.user.id)
            newCampaign = Campaign(
                name=name,
                shortDescription=shortDescription,
                goal=goal,
                expiredDate=expiredDate,
                coverImage=coverImage,
                fullDescription=fullDescription,
                ownerID=ownerID)

            newCampaign.save()
            #csrf_token = django.middleware.csrf.get_token(request)
            # redirect to a new URL:
            return render(None, 'vdf/thankyou.html', {"user": request.user.id})

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = AddCampaignForm()
    #csrf_token = django.middleware.csrf.get_token(request)
    #return render(None, 'vdf/taochiendich.html', {"user": request.user.id})
    return redirect('/taochiendich')

