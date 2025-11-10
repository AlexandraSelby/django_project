# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from reviews.views import LoginWithMessage 
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("reviews/", include("reviews.urls")),
    path("accounts/login/",  LoginView.as_view(),  name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"), # <-- swap in built-in
    path("accounts/", include("django.contrib.auth.urls")),
    path("", RedirectView.as_view(pattern_name="reviews:home", permanent=False), name="root"),
]
