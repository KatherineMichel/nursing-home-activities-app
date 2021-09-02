from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from rest_framework import viewsets
from django_filters import rest_framework as filters

from activities.models import Activity, Resident
from activities.serializers import (
    ActivitySerializer,
    ResidentSerializer,
    UserSerializer,
)


class ActivityFilter(filters.FilterSet):
    start = filters.DateTimeFromToRangeFilter(
        field_name="start",
        lookup_expr="gte",
        label="Activity starts on or after and on or before",
    )

    class Meta:
        model = Activity
        fields = ["start"]


class IndexView(TemplateView):

    template_name = "index.html"


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ActivityFilter


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
