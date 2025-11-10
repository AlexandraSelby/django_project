# reviews/models.py
# Defines the Review model that stores perfume reviews linked to users.

from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model  # link reviews to a user model dynamically


class Review(models.Model):
    # --------------------------------------------------------
    # Author: the user who created this review.
    # - ForeignKey links each review to a Django User.
    # - CASCADE means if a user is deleted, their reviews go too.
    # - null=True + blank=True allow existing reviews without an author
    #   (important for backward compatibility with older data).
    # --------------------------------------------------------
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reviews",
        null=True,
        blank=True,
        help_text="User who wrote this review",
    )

    # --------------------------------------------------------
    # Core review fields
    # --------------------------------------------------------
    brand = models.CharField(max_length=80)                # Perfume house or brand
    fragrance_name = models.CharField(max_length=120)      # Name of the fragrance
    rating = models.PositiveSmallIntegerField()            # 1–5 rating scale
    body = models.TextField()                              # Full review text
    created = models.DateTimeField(auto_now_add=True)      # Auto timestamp on creation

    # --------------------------------------------------------
    # Meta data and string representation
    # --------------------------------------------------------
    class Meta:
        ordering = ["-created"]  # Show newest reviews first

    def __str__(self):
        # Human-readable summary for admin and debugging
        return f"{self.brand} {self.fragrance_name} ({self.rating}/5)"

    # --------------------------------------------------------
    # Canonical URL for linking to individual reviews
    # Used by templates and redirects
    # --------------------------------------------------------
    def get_absolute_url(self):
        """Canonical URL for this review (used by templates/links)."""
        return reverse("reviews:detail", args=[self.pk])
