from django.contrib import admin
from article.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'article_date', 'article_author',)


# Register your models here.

admin.site.register(Article, ArticleAdmin)
