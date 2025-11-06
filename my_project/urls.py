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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # simple root redirect to a named URL

urlpatterns = [
    path("admin/", admin.site.urls),
    path("reviews/", include("reviews.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    # Redirect "/" → reviews home (non-permanent so browsers don’t cache it)
    path("", RedirectView.as_view(pattern_name="reviews:home", permanent=False), name="root"),
]
