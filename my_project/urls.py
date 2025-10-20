# my_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),   # Django admin
    path("", include("reviews.urls")), # Mount ONLY the reviews app at the site root
]
