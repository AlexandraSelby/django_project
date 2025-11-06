from django.test import TestCase
from django.urls import reverse

class HomeViewSmokeTest(TestCase):
    def test_home_returns_200(self):
        url = reverse("reviews:home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
from django.test import TestCase
from django.urls import reverse
from .models import Review

class DetailViewSmokeTest(TestCase):
    def setUp(self):
        self.review = Review.objects.create(
            brand="Khadlaj",
            fragrance_name="Fursan White",
            rating=4,
            body="Test body"
        )

    def test_detail_returns_200(self):
        url = reverse("reviews:detail", args=[self.review.pk])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
