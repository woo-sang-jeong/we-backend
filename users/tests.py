from rest_framework.test import APITestCase


class TestUsers(APITestCase):
    def test_plus(self):
        self.assertEqual(2 + 2, 4, "wrong!")
