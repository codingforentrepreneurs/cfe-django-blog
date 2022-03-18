from django.urls import path

from . import views

app_name = "articles"
urlpatterns = [
    path("<slug:slug>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("", views.ArticleListView.as_view(), name="article-list"),
]
