from django.db import models

from django.db import models

class Review(models.Model):
    brand = models.CharField(max_length=80)
    fragrance_name = models.CharField(max_length=120)
    rating = models.PositiveSmallIntegerField()  # 1–5 later
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.brand} {self.fragrance_name} ({self.rating}/5)"
