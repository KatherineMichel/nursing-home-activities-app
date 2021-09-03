from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from .models import Activity, Resident
from .views import ActivityViewSet


class TestModel(TestCase):
    def test_group_026_model(self):
        activity = baker.make(Activity)
        assert activity.name
        assert activity.description
        assert activity.start
        assert activity.end
        assert activity.location
        assert activity.options
        assert activity.residents

    def test_group_028_model(self):
        resident = baker.make(Resident)
        assert resident.user
        assert resident.activity
        assert resident.status


class ActivityTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.list_view = ActivityViewSet.as_view({"get": "list"})
        self.create_view = ActivityViewSet.as_view({"post": "create"})
        self.uri = "/activities/"

    def test_user_able_to_access_list_of_activities(self):
        request = self.factory.get(self.uri)
        response = self.list_view(request)
        self.assertTrue(isinstance(response.data, list))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
