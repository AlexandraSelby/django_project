# reviews/urls.py
# Routes that belong to the "reviews" app.

from django.urls import path
from . import views

app_name = "reviews"                      # lets us reverse URLs like 'reviews:home'

urlpatterns = [
    path("", views.home, name="home"),    # "/" -> reviews.views.home  (homepage)
    path("<int:pk>/", views.detail, name="detail"),  # "/1/" -> reviews.views.detail
]
