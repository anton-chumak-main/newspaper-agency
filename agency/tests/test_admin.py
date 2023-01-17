from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="Test username",
            first_name="Test first name",
            last_name="Test last name",
            password="test1234",
            years_of_experience=15
        )

    def test_redactor_years_of_experience_listed(self):
        url = reverse("admin:agency_redactor_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.redactor.years_of_experience)

    def test_redactor_detailed_years_of_experience_listed(self):
        url = reverse("admin:agency_redactor_change", args=[self.redactor.id])
        res = self.client.get(url)

        self.assertContains(res, self.redactor.years_of_experience)

    def test_driver_additional_info_field_detailed(self):
        url = reverse("admin:agency_redactor_add")
        res = self.client.get(url)

        self.assertContains(res, "Additional info")
