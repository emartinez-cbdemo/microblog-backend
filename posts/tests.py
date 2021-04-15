from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Post, User


class PostTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create(username="dinkleberg")

    def test_create_post(self):
        user = User.objects.get(username="dinkleberg")
        Post.objects.create(user=user, message="Hello, world!")
        post = Post.objects.get(user=user)
        self.assertEqual(post.message, "Hello, world!")


class PostAPITests(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create(username="dinkleberg")
        Post.objects.create(user=user, message="Hello, universe!")
        Post.objects.create(user=user, message="Hello, world!")

    def test_get_posts(self):
        url = reverse("post-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.data[1]["message"], "Hello, universe!")
        self.assertEqual(response.data[0]["message"], "Hello, world!")
