from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article


# View for viewing all posted articles as a list
class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


# View for viewing one specific article in detail
class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


# View for editing an article
class ArticleUpdateView(UpdateView):
    model = Article
    # fields to be presented for user editing
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"


# View for deleting an article
class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    # redirect to article list page upon success
    success_url = reverse_lazy("article_list")


# View for creating a new article
class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )
