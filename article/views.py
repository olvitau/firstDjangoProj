from django.shortcuts import render, get_object_or_404
from article.models import Article


# Create your views here.


def home(request):
    articles = Article.objects.all()[:5]
    return render(request, 'article/articles_list.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article/article_detail.html', {'article': article})
