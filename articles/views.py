from django.views import generic

from .models import Article


class ArticleHomeView(generic.ListView):
    queryset = Article.objects.published()
    paginate_by = 10
    template_name = "articles/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Latest Articles"
        return context


class ArticleListView(generic.ListView):
    queryset = Article.objects.published()
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")
        if query is not None:
            return qs.search(query=query)
        return qs


class ArticleDetailView(generic.DetailView):
    queryset = Article.objects.published()
