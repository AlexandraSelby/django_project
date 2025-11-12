# reviews/forms.py
# ModelForm for creating a new Review. (View wiring comes next.)

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    """
    Minimal form to create a Review.
    - Validates rating as 1–5
    - Keeps labels user-friendly
    """
    class Meta:
        model = Review
        fields = ["brand", "fragrance_name", "rating", "body", "video_url"]
        labels = {
            "brand": "Brand",
            "fragrance_name": "Fragrance name",
            "rating": "Rating (1–5)",
            "body": "Your review",
            
        }

    def clean_rating(self):
        r = self.cleaned_data.get("rating")
        if r is None or not (1 <= r <= 5):
            raise forms.ValidationError("Please enter a rating between 1 and 5.")
        return r
