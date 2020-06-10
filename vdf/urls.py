from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("articles", views.articles, name="articles"),
    path("explore_pages", views.explore_pages, name="explore_pages"),
    path("explore_result", views.explore_result, name="explore_result"),
    path("explore", views.explore, name="explore"),
    path("thankyou", views.thankyou, name="thankyou"),
    path("faq", views.faq, name="faq"),
    path("faqs", views.faqs, name="faqs"),
    path("contact", views.contact, name="contact"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("project_detail", views.project_detail, name="project_detail"),
    path("register", views.register, name="register"),
    path("resetpassword", views.resetpassword, name="resetpassword"),
    path("taochiendich", views.taochiendich, name="taochiendich"),
    path("donate", views.donate, name="donate"),
    path("admin/campaign", views.AdminCampaign, name="adminCampaign"),
    path("admin/show-user", views.AdminShowUser, name="adminShowUser"),
    path("admin/edit", views.AdminUserEdit, name="adminUserEdit"),
    path("admin/changepassword", views.AdminChangePassword, name="AdminChangePassword"),
    path("supadmin/showusers",views.supAdminshowUsers, name="supAdminshowUsers"),
    path("supadmin/edit",views.supAdminEdit,name="supAdminEdit"),
    path("supadmin/showdetails",views.supAdminShowDetails,name="supAdminShowDetails"),
    path("supadmin/campaign",views.supAdminCampaign,name="supAdminCampaign"),
    path("supadmin/supAdminadduser",views.supAdminadduser,name="supAdminadduser"),
    path("supadmin/feedback",views.Feedback,name="Feedback"),
    path("AddCampaign",views.AddCampaignProcess, name="AddCampaignProcess")
    # path("<str:name>", views.greet, name="greet")
]