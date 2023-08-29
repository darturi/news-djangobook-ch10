from django.db import models
from django.conf import settings
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        # AUTH_USER_MODEL refers to our custom user model
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    # Many to one relationship with article (many = comment, one = article)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # Makes comment a CharField with a character limit of 140
    comment = models.CharField(max_length=140)
    # Sets the comment author to our custom user model
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    # Will return the comment content as a string
    def __str__(self):
        return self.comment

    # Will return the url associated with "article_list"
    def get_absolute_url(self):
        return reverse("article_list")
