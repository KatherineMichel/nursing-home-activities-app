from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from rest_framework import viewsets

from activities.serializers import (
    UserSerializer,
)


class HomePageView(TemplateView):

    template_name = "home.html"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
