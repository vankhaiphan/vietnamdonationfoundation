from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("articles", views.about, name="articles"),
    path("explore_pages", views.about, name="explore_pages"),
    path("explore_result", views.about, name="explore_result"),
    path("explore", views.about, name="explore"),
    path("login", views.about, name="login"),
    path("project_detail", views.about, name="project_detail"),
    path("register", views.about, name="register"),
    path("taochiendich", views.about, name="taochiendich"),
    # path("<str:name>", views.greet, name="greet")
]