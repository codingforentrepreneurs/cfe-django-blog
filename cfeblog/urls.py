from articles.views import ArticleHomeView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", ArticleHomeView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("articles/", include("articles.urls")),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
