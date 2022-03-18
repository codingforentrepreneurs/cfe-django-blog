from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "is_published"]
    raw_id_fields = ["user"]
    list_filter = [
        "publish_status",
        "user_publish_timestamp",
        "publish_timestamp",
        "updated",
        "timestamp",
    ]
    readonly_fields = [
        "publish_timestamp",
        "updated_by",
        "updated",
        "timestamp",
    ]

    class Meta:
        model = Article

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
