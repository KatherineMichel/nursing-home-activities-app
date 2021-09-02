from django.urls import path

from rest_framework.schemas import get_schema_view

from activities.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path(
        "openapi",
        get_schema_view(
            title="Nursing Home Activities API",
            description="API for activities and residents",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
]