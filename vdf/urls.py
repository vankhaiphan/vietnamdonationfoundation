from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("articles", views.article, name="articles"),
    path("explore_pages", views.explore_pages, name="explore_pages"),
    path("explore_result", views.explore_result, name="explore_result"),
    path("explore", views.explore, name="explore"),
    path("login", views.login, name="login"),
    path("project_detail", views.project_detail, name="project_detail"),
    path("register", views.register, name="register"),
    path("taochiendich", views.taochiendich, name="taochiendich"),
    # path("<str:name>", views.greet, name="greet")
]