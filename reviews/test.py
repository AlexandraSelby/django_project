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

from django.test import TestCase
from django.urls import reverse

class RootRedirectTest(TestCase):
    def test_root_redirects_to_reviews_home(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.headers["Location"], reverse("reviews:home"))

class LoginPageTest(TestCase):
    def test_login_page_returns_200(self):
        resp = self.client.get("/accounts/login/")
        self.assertEqual(resp.status_code, 200)

# reviews/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class NewReviewAccessTest(TestCase):
    def test_anonymous_is_redirected_to_login(self):
        resp = self.client.get(reverse("reviews:new"))
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/accounts/login/", resp.headers["Location"])

    def test_logged_in_gets_200(self):
        User.objects.create_user(username="alice", email="a@example.com", password="pw12345")
        self.client.login(username="alice", password="pw12345")
        resp = self.client.get(reverse("reviews:new"))
        self.assertEqual(resp.status_code, 200)
        
