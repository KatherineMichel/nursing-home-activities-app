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


class ResidentFilter(filters.FilterSet):
    class Meta:
        model = Resident
        fields = ["activity__id", "status"]


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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ResidentFilter
    # filter_fields = ("activity__id", "status")

    # http://127.0.0.1:8000/residents/?activity__id=1&status=going

    """
    def get_queryset(self):
        queryset = Activity.objects.all()
        activity = self.request.query_params.get("activity__id")
        status = self.request.query_params.get("status")
        if activity is not None:
            queryset = queryset.filter(activity=activity, status=status)
    """


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
