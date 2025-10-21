# reviews/views.py
from django.shortcuts import render, get_object_or_404
from .models import Review

def home(request):
    # Newest 20 reviews
    reviews = Review.objects.order_by("-created")[:20]
    return render(request, "reviews/home.html", {"reviews": reviews})

def detail(request, pk: int):
    review = get_object_or_404(Review, pk=pk)  # returns 404 if not found
    return render(request, "reviews/detail.html", {"review": review})

