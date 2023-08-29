from typing import Any, Dict, Optional
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article
from .forms import CommentForm


# View for viewing all posted articles as a list
class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"


class CommentGet(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Article
    # passes form name to FormView
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        # gets article pk
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    # called when form validation is a success
    def form_valid(self, form):
        comment = form.save(commit=False)
        # specify the article the comment belongs to
        comment.article = self.object
        # specify the author of the comment by fetching user
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    # after comment is posted redirect to detail view of the article
    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs={"pk": article.pk})


# View for viewing one specific article in detail
class ArticleDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


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
