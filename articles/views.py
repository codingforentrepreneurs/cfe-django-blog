from django.views import generic

from .models import Article


class ArticleListView(generic.ListView):
    queryset = Article.objects.published()
