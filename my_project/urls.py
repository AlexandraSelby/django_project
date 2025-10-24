# my_project/urls.py
# Project-level URL routes: admin and the reviews app.

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # tiny helper to redirect one URL to another (302/301)



# Map URLs to views. Keep routes small and obvious.

urlpatterns = [
    path("admin/", admin.site.urls),                 # Django admin at /admin/
    path("reviews/", include("reviews.urls")),       # Mount the reviews app at /reviews/
    # Example: /reviews/ → home view, /reviews/1/ → detail view 
    path("accounts/", include("django.contrib.auth.urls")),  # Login/Logout/Password views
]

