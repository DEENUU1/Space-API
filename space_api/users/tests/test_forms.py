from django.test import TestCase
from users.forms import CreateUserForm


class TestForm(TestCase):

    def test_create_user_form_valid_data(self):
        """
        Test that the CreateUserForm is valid when given valid input data
        """
        form = CreateUserForm(data={
            'username': 'test',
            'email': 'test@example.com',
            'password1': 'Test123@',
            'password2': 'Test123@'
        })

        self.assertTrue(form.is_valid())

    def test_create_user_form_no_data(self):
        """
        Test that the CreateUserForm is invalid when given no input data
        """
        form = CreateUserForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
