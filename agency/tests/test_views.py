from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from agency.models import Topic, Newspaper, Redactor

TOPICS_URL = reverse("agency:topic-list")
NEWSPAPERS_URL = reverse("agency:newspaper-list")
REDACTORS_URL = reverse("agency:redactor-list")


class PublicTopicTestForm(TestCase):
    def test_login_required(self):
        res = self.client.get(TOPICS_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "user.test",
            "passwordtest123"
        )
        self.client.force_login(self.user)

    def test_retrieve_topics(self):
        Topic.objects.create(name="Crime")
        Topic.objects.create(name="Weather")

        response = self.client.get(TOPICS_URL)
        topics = Topic.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topics)
        )
        self.assertTemplateUsed(response, "agency/topic_list.html")


class PrivateNewspaperTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "user.test",
            "passwordtest123"
        )
        self.client.force_login(self.user)

    def test_retrieve_newspapers(self):
        topic = Topic.objects.create(name="Crime")

        Newspaper.objects.create(
            title="Test name newspaper",
            context="Test content",
            published_date='02-02-2020',
            topic=topic
        )

        response = self.client.get(NEWSPAPERS_URL)
        newspapers = Newspaper.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(newspapers)
        )
        self.assertTemplateUsed(response, "agency/newspaper_list.html")


class PublicRedactorTestForm(TestCase):
    def test_login_required(self):
        res = self.client.get(REDACTORS_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "user.test",
            "passwordtest123"
        )
        self.client.force_login(self.user)

    def test_retrieve_drivers(self):
        Redactor.objects.create(years_of_experience=12)

        response = self.client.get(REDACTORS_URL)
        driver = Redactor.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["redactor_list"]),
            list(driver)
        )
        self.assertTemplateUsed(response, "agency/redactor_list.html")
