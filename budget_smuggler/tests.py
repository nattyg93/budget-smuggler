from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.utils.timezone import now
from rest_framework import status, test

from . import models

User = get_user_model()


class APIClient(test.APIClient):
    api_base = '/backend/api/v1/'

    def _get_path(self, parsed):
        path = super()._get_path(parsed)
        if path[0] == '/':
            path = (self.api_base or '') + path[1:]
        return path


class APITestCase(test.APITestCase):
    client_class = APIClient

    def _auth(self, user):
        self.current_user = user
        self.client.force_authenticate(user)

    def _give_user_perm(self, user, perm):
        app_label, codename = perm.split('.')
        user.user_permissions.add(
            Permission.objects.filter(
                content_type__app_label=app_label, codename=codename).first())
        user.save()


class ExpenseTestCase(APITestCase):
    def setUp(self):
        self._auth(User.objects.create(email='test@example.com'))

    def get_default_data(self, api=True):
        data = {
            'date': now(),
            'cost': 5.20,
            'item': 'Coffee',
            'location': '',
            'notes': '',
        }
        if api:
            data['date'] = data['date'].isoformat()
        else:
            data['user'] = self.current_user
        return data

    def test_get_expenses(self):
        expense = models.Expense.objects.create(**self.get_default_data(False))
        response = self.client.get('/expenses/')
        results = response.json()['results']
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['id'], expense.pk)

    def test_fail_without_auth(self):
        self._auth(None)
        response = self.client.post('/expenses/', data=self.get_default_data())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_expense(self):
        response = self.client.post('/expenses/', data=self.get_default_data())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_own_expenses_only(self):
        models.Expense.objects.create(**self.get_default_data(False))
        self._auth(User.objects.create(email='new_user@example.com'))
        pk = models.Expense.objects.create(**self.get_default_data(False)).pk
        response = self.client.get('/expenses/')
        results = response.json()['results']
        self.assertTrue(len(results), 1)
        self.assertTrue(results[0]['id'], pk)
