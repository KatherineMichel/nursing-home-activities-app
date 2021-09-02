from django.urls import path

from activities.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
