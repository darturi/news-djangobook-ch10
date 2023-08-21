"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # included for url consistency in the sign up page and log in log out
    # and we must create our own sign up
    path("accounts/", include("accounts.urls")),
    # included so we can utilize the built in log in and log out views
    path("accounts/", include("django.contrib.auth.urls")),
    # url path for articles
    path("articles/", include("articles.urls")),
    # Path for the new home page as stored in the pages app
    path("", include("pages.urls")),
]
