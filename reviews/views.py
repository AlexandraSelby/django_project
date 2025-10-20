from django.http import HttpResponse

from django.shortcuts import render
from .models import Review

def home(request):
    reviews = Review.objects.order_by("-created")[:20]
    return render(request, "reviews/home.html", {"reviews": reviews})


