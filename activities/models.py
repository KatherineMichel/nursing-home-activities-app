from django.db import models
from django.contrib.auth.models import User


LOCATION_OPTIONS = [
    ("activity room", "activity room"),
    ("skilled nursing", "skilled nursing"),
    ("assisted living", "assisted living"),
    ("memory care", "memory care"),
    ("dining room", "dining room"),
    ("outing", "outing"),
]

ACTIVITY_OPTIONS = [
    ("virtual", "virtual"),
    ("in person", "in person"),
    ("both", "both"),
]

STATUS_OPTIONS = [
    ("going", "going"),
    ("not going", "not going"),
    ("maybe", "maybe"),
]


class Activity(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=255, blank=True, null=True, default="")
    start = models.DateTimeField()
    end = models.DateTimeField()
    location = models.CharField(
        choices=LOCATION_OPTIONS, default="dining room", max_length=100
    )
    options = models.CharField(choices=ACTIVITY_OPTIONS, default="both", max_length=100)
    residents = models.ManyToManyField(
        "Resident", blank=True, null=True, related_name="activities"
    )


class Resident(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="activity"
    )
    status = models.CharField(
        choices=STATUS_OPTIONS, default="not going", max_length=100
    )
