from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Article(models.Model):
    article_title = models.CharField(max_length=255, verbose_name=u'Заголовок', name=u'article_title')
    article_text = models.TextField(verbose_name=u'Текст', name=u'article_text')
    article_date = models.DateTimeField(verbose_name=u'Дата добавления', name=u'article_date')
    article_author_id = models.ForeignKey(to=User, verbose_name=u'Автор', name=u'article_author', null=False,
                                          blank=False)

    @property
    def __unicode__(self):
        return self.article_title

    class Meta():
        db_table = u'articles'
        ordering = ('article_date',)
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
