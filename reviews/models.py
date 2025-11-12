# reviews/models.py
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model  # Link reviews to the user who wrote them


class Review(models.Model):
    """
    Core review entity for the app.

    Fields:
    - author: who wrote the review (used for edit/delete ownership checks)
    - brand: perfume brand (e.g., "Khadlaj")
    - fragrance_name: fragrance name (e.g., "Fursan White")
    - rating: integer score (1–5)
    - body: free-text review content
    - video_url: optional YouTube/TikTok/Instagram URL for embedded video
    - created: timestamp when the review was created

    Notes:
    - author is nullable on purpose so old rows/migrations don't break;
      new posts will set author in the view to request.user.
    """

    # Who created this review (needed for edit/delete permissions).
    # null=True for existing rows; we’ll enforce non-null on new posts in the view.
    # class Review(models.Model):
    # Who created this review (needed for edit/delete permissions).
    
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
    rating = models.PositiveSmallIntegerField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.brand} {self.fragrance_name} ({self.rating}/5)"

    def get_absolute_url(self):
        """Canonical URL for this review (used by templates/links)."""
        return reverse("reviews:detail", args=[self.pk])

    # --- YouTube helper (no DB change needed) --------------------------------
    # If the review body contains a YouTube link (watch, youtu.be, shorts, embed),
    # return an embeddable <iframe> src like: https://www.youtube.com/embed/VIDEO_ID
    # Used in the detail template via: {% with review.youtube_embed_src_auto as yt %}

    import re
    from urllib.parse import urlparse, parse_qs

    _YT_ID_RE = re.compile(
        r"""(?ix)
        (?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|shorts/))
        ([A-Za-z0-9_-]{6,})     # video id
        """
    )

    @classmethod
    def _extract_youtube_id(cls, text: str) -> str | None:
        if not text:
            return None

        # 1) Quick regex scan (covers youtu.be, /embed/, /shorts/, watch?v=)
        m = cls._YT_ID_RE.search(text)
        if m:
            return m.group(1)

        # 2) Robust parse for full URLs (keeps query like ?si=… from breaking it)
        for token in text.split():
            try:
                u = cls.urlparse(token)
            except Exception:
                continue
            host = (u.netloc or "").lower()
            if "youtube.com" in host and u.path == "/watch":
                vid = cls.parse_qs(u.query).get("v", [None])[0]
                if vid:
                    return vid
            if "youtu.be" in host and u.path.strip("/"):
                return u.path.strip("/")

        return None

    @property
    def youtube_embed_src_auto(self) -> str | None:
        """
        If we can find a YouTube video ID in the review text,
        return an embeddable player URL. Otherwise None.
        """
        vid = self._extract_youtube_id(self.body)
        if not vid:
            return None
        return f"https://www.youtube.com/embed/{vid}?rel=0"