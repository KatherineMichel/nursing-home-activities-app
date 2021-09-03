from django.test import TestCase
from model_bakery import baker

from .models import (
    Activity,
    Resident
)


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
