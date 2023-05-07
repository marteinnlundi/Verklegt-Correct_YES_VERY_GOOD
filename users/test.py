from django.test import TestCase, Client

class EditProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_edit_profile_view(self):
        response = self.client.get('/users/edit_profile')
        self.assertEqual(response.status_code, 200)