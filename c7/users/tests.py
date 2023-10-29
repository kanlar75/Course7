from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserCreateTestCase(APITestCase):
    def setUp(self):
        pass

    def test_user_create(self):
        data = {
            'email': 'user@test.com',
            'password': '12345',
            'chat_id': '5095728080'
        }

        response = self.client.post(
            reverse('users:user_create'),
            data=data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserListTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='user@test.com',
            password='12345',
            chat_id='5095728080'
        )

    def test_users_list(self):
        response = self.client.get(
            reverse('users:user_list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserRetrieveTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='user@test.com',
            password='12345',
            chat_id='5095728080'
        )

    def test_user_retrieve(self):
        response = self.client.get(
            reverse('users:user_detail',
                    args=[self.user.pk])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserUpdateTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='user@test.com',
            password='12345',
            chat_id='5095728080'
        )

    def test_user_update(self):
        data = {
            'username': 'test_test',
        }
        response = self.client.patch(
            reverse('users:user_update',
                    args=[self.user.pk]),
            data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UserDestroyTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            email='user@test.com',
            password='12345',
            chat_id='5095728080'
        )

    def test_user_destroy(self):
        response = self.client.delete(
            reverse('users:user_delete',
                    args=[self.user.pk]),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
