from django.urls import path
from .views import HomePageView

urlpatterns = [
    # url path for the homepage using the view we created for it
    path("", HomePageView.as_view(), name="home"),
]
