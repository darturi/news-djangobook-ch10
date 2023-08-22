from typing import Optional
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article


# View for viewing all posted articles as a list
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"


# View for viewing one specific article in detail
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"


# View for editing an article
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    # fields to be presented for user editing
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    # Tests if the author of the article is the same as the user
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# View for deleting an article
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    # redirect to article list page upon success
    success_url = reverse_lazy("article_list")

    # Tests if the author of the article is the same as the user
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


# View for creating a new article
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
    )

    # Makes it so the author of a given article is set to the logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
