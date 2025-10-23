# reviews/views.py
from django.shortcuts import render, get_object_or_404
from .models import Review

def home(request):
    # Newest 20 reviews
    reviews = Review.objects.only("brand", "fragrance_name", "rating", "body", "created")[:20]
    return render(request, "reviews/home.html", {"reviews": reviews})

def detail(request, pk: int):
    review = get_object_or_404(Review, pk=pk)  # returns 404 if not found
    return render(request, "reviews/detail.html", {"review": review})

# --- Signup (user registration) ---
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def signup(request):
    """
    Simple user registration using Django's built-in UserCreationForm.
    On success, redirect to the login page.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # built-in auth route
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
