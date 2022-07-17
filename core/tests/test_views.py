from django.test import TestCase, Client
from django.shortcuts import render


class RegisterTestCase(TestCase):

    def setUp(self) -> None:
        self.data = {
            'username': 'ze',
            'email': 'em123456mail8910@gmail.com',
            'password': 'senha1234senha',
            'c_password': 'senha1234senha',
        }
        self.client = Client()

    def into_page(self):
        request = self.client.get('/signup/')
        self.assertEqual(request.status_code, 200)

    def test_form_valid(self):
        request = self.client.post('/login/', data=self.data)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        wrong_data = {
            'password': 'senha123',
            'c_password': '123senha',
        }

        request = self.client.post('/signup/', data=wrong_data)
        self.assertEqual(request.status_code, 302)


class SigninTestCase(TestCase):

    def setUp(self) -> None:
        self.data = {
            'username': 'dummy',
            'password': 'dummy123',
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post('/login/', data=self.data)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        wrong_data = {
            'username': 'dummy',
            'password': 'qualquer123',
        }

        request = self.client.post('/login/', data=wrong_data)
        self.assertEqual(request.status_code, 302)