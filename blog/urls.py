from django.urls import path

from blog.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
]
