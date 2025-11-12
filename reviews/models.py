# reviews/models.py

from django.db import models  # ✅ make sure this stays at the top
from django.urls import reverse
from django.contrib.auth import get_user_model  # link reviews to a user
from urllib.parse import urlparse, parse_qs
import re


class Review(models.Model):
    # Who created this review (needed for edit/delete permissions).
    # null=True for existing rows; we’ll enforce non-null on new posts in the view.
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reviews",
        null=True,
        blank=True,
        help_text="User who wrote this review",
    )

    brand = models.CharField(max_length=80)
    fragrance_name = models.CharField(max_length=120)
    rating = models.PositiveSmallIntegerField()  # 1–5 later
    body = models.TextField()

    # --- FIX: ADDED MISSING FIELD ------------------------------------------------
    # This field was missing, causing the FieldError in ReviewForm.
    video_url = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        help_text="Optional video URL, not currently used by embed logic below.",
    )
    # -----------------------------------------------------------------------------

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.brand} {self.fragrance_name} ({self.rating}/5)"

    def get_absolute_url(self):
        """Canonical URL for this review (used by templates/links)."""
        return reverse("reviews:detail", args=[self.pk])

    # --------------------------------------------------------------
    # Optional YouTube embed helpers (safe for templates)
    # These functions let users paste a YouTube link into their review body.
    # When the page renders, we extract the video ID and build a safe
    # embedded <iframe> URL for inline playback.
    # --------------------------------------------------------------
    @property
    def youtube_embed_src_auto(self):
        """
        Look for a YouTube link in the review body and return an
        embeddable src URL (or None if nothing usable is found).
        Safe to access in templates.
        """
        text = self.body or ""
        # The regex below looks for *any* URL, which is then passed to _youtube_to_embed.
        match = re.search(r"https?://[^\s)]+", text)
        if not match:
            return None
        return self._youtube_to_embed(match.group(0))

    @staticmethod
    def _youtube_to_embed(url: str | None) -> str | None:
        """
        Convert a standard YouTube URL (youtu.be or youtube.com/watch?v=)
        into an embeddable https://www.youtube.com/embed/<id> form.
        Returns None if url is not a YouTube link.
        """
        if not url:
            return None
        try:
            parsed = urlparse(url)
            host = parsed.netloc.lower()
            video_id = None

            if "youtu.be" in host:
                # Example: https://youtu.be/VIDEOID?si=...
                video_id = parsed.path.lstrip("/")
            elif "youtube.com" in host:
                # Example: https://www.youtube.com/watch?v=VIDEOID
                qs = parse_qs(parsed.query)
                video_id = (qs.get("v") or [None])[0]

            if not video_id:
                return None

            # Handle start time if provided (?t=123 or ?start=123)
            qs = parse_qs(parsed.query)
            start = (qs.get("t") or qs.get("start") or [None])[0]
            if start:
                start = start.replace("s", "")

            # Set ?rel=0 to prevent related videos from other channels after playback
            src = f"https://www.youtube.com/embed/{video_id}?rel=0"
            if start:
                # Add start time, handling existing query string
                sep = "&" if "?" in src else "?"
                src = f"{src}{sep}start={start}"

            return src
        except Exception:
            return None