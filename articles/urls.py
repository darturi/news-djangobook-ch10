from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
)

urlpatterns = [
    # url path for viewing a single article
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    # url path for editing an article
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    # url path for deleting an article
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
    # url path for creating an article
    path("new", ArticleCreateView.as_view(), name="article_new"),
    # url path for viewing all the articles as a list
    path("", ArticleListView.as_view(), name="article_list"),
]
