from django.conf import settings
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone

from . import utils

User = settings.AUTH_USER_MODEL  # defaults to 'auth.User'


class ArticleQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_status=Article.ArticlePublishOptions.PUBLISH).filter(
            Q(publish_timestamp__lte=now) | Q(user_publish_timestamp__lte=now)
        )

    def pending_published(self):
        now = timezone.now()
        return self.filter(publish_status=Article.ArticlePublishOptions.PUBLISH).filter(
            Q(publish_timestamp__gt=now) | Q(user_publish_timestamp__gt=now)
        )

    def drafts(self):
        return self.filter(publish_status=Article.ArticlePublishOptions.DRAFT)

    def select_author(self):
        return self.select_related("user")

    def search(self, query=None):
        if query is None:
            return self.none()
        return self.filter(Q(title__icontains=query) | Q(content__icontains=query))


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published().select_author()

    def drafts(self):
        return self.get_queryset().drafts().select_author()

    def pending(self):
        return self.get_queryset().pending_published().select_author()


class Article(models.Model):
    class ArticlePublishOptions(models.TextChoices):
        PUBLISH = "pub", "Publish"
        DRAFT = "dra", "DRAFT"
        PRIVATE = "pri", "Private"

    user = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    updated_by = models.ForeignKey(
        User, related_name="editor", null=True, blank=True, on_delete=models.SET_NULL
    )
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=utils.get_article_image_upload_to, null=True, blank=True
    )
    publish_status = models.CharField(
        max_length=3,
        choices=ArticlePublishOptions.choices,
        default=ArticlePublishOptions.DRAFT,
    )
    publish_timestamp = models.DateTimeField(
        help_text="Field-driven publish timestamp",
        auto_now_add=False,
        auto_now=False,
        blank=True,
        null=True,
    )
    user_publish_timestamp = models.DateTimeField(
        help_text="User-defined publish timestamp",
        auto_now_add=False,
        auto_now=False,
        blank=True,
        null=True,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ArticleManager()

    class Meta:
        ordering = ["-user_publish_timestamp", "-publish_timestamp", "-updated"]

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"slug": self.slug})

    def get_image_url(self):
        if not self.image:
            return None
        return self.image.url

    @property
    def is_published(self):
        if not self.publish_status == Article.ArticlePublishOptions.PUBLISH:
            return False
        now = timezone.now()
        if self.user_publish_timestamp is not None:
            return self.user_publish_timestamp <= now
        return self.publish_timestamp <= now

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = utils.unique_slug_generator(self)
        if self.user_publish_timestamp:
            """
            User has set user_publish_timestamp,
            Automatically set publish_timestamp
            """
            self.publish_timestamp = self.user_publish_timestamp
        if self.publish_status == Article.ArticlePublishOptions.PUBLISH:
            """
            User has set publish_status to PUBLISH,
            Automatically set publish_timestamp to
            now
            """
            if not self.publish_timestamp:
                self.publish_timestamp = timezone.now()
        super().save(*args, **kwargs)
