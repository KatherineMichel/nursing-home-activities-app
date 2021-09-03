from django.contrib.auth.models import User
from rest_framework import serializers

from activities.models import Activity, Resident


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = "__all__"


class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = "__all__"


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ("url", "id", "username", "events")
