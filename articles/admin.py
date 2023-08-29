from django.contrib import admin
from .models import Article, Comment


class CommentInLine(admin.TabularInline):
    # The model being used for the comments
    model = Comment
    # The number of extra empty comment slots you will see on the admin page
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body",
        "author",
    ]
    # data on how to display comments related to an article in admin
    inlines = [
        CommentInLine,
    ]


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
