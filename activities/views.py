from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from rest_framework import viewsets

from activities.models import Activity
from activities.serializers import (
    ActivitySerializer,
    UserSerializer,
)


class IndexView(TemplateView):

    template_name = "index.html"


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
