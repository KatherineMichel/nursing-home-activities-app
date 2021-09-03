from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from activities import views
from activities.views import IndexView

router = DefaultRouter()
router.register(r"activities", views.ActivityViewSet)
router.register(r"residents", views.ResidentViewSet)
router.register(r"users", views.UserViewSet)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("api/", include(router.urls)),
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
