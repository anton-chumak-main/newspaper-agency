from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper, Redactor


class ModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(
            username="Test username",
            password="test1234",
            first_name="Test firstname",
            last_name="Test lastname",
            years_of_experience=12,
        )

        topic = Topic.objects.create(
            name="Test",

        )

        Newspaper.objects.create(
            title="Test model",
            context="Test context",
            topic=topic
        )

    def test_topic_str(self):
        topic = Topic.objects.get(id=1)

        self.assertEqual(
            str(topic), topic.name
        )

    def test_redactor_str_and_password(self):
        redactor = get_user_model().objects.get(id=1)

        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )
        self.assertTrue(redactor.check_password("test1234"))

    def test_get_absolute_url(self):
        redactor = get_user_model().objects.get(id=1)

        self.assertEquals(redactor.get_absolute_url(), "/redactors/1")

    def test_first_name_label(self):
        redactor = Redactor.objects.get(id=1)
        field_label = redactor._meta.get_field("first_name").verbose_name

        self.assertEquals(field_label, "first name")

    def test_create_redactor_years_of_experience(self):
        redactor = get_user_model().objects.get(id=1)

        self.assertEqual(redactor.years_of_experience, 12)

    def test_newspaper_str(self):
        newspaper = Newspaper.objects.get(id=1, topic_id=1)

        self.assertEqual(str(newspaper), "Test model Test context (2023-01-17)")
