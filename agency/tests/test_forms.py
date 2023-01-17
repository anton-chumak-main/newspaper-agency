from django.test import TestCase

from agency.forms import RedactorCreationForm


class DriverFormTest(TestCase):

    def test_driver_form_is_valid(self) -> None:
        form_data = {
            "username": "test",
            "password1": "user1234",
            "password2": "user1234",
            "first_name": "Test first name",
            "last_name": "Test last name",
            "years_of_experience": 12
        }
        form = RedactorCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
