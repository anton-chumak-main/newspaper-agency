from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Redactor, Newspaper, Topic


class SearchTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "TestUser",
            "password123"
        )
        self.client.force_login(self.user)

    def test_search_redactor_by_name(self):
        response = self.client.get(
            reverse("agency:redactor-list") + "?username=TestUser"
        )

        self.assertEqual(
            list(response.context["redactor_list"]),
            list(Redactor.objects.filter(username__icontains="TestUser")),
        )

    def test_search_topic_by_title(self):
        response = self.client.get(
            reverse("agency:topic-list") + "?name=TestName"
        )

        self.assertEqual(
            list(response.context["topic_list"]),
            list(Topic.objects.filter(name__icontains="TestName")),
        )

    def test_search_newspaper_by_title(self):
        response = self.client.get(
            reverse("agency:newspaper-list") + "?title=TestTitle"
        )

        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(Newspaper.objects.filter(title__icontains="TestTitle")),
        )
