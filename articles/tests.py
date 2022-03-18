from django.conf import settings
from django.test import TestCase

from .models import Article

FIXTURES_DIR = settings.BASE_DIR / "fixtures"


class ArticleTestCase(TestCase):
    fixtures = [FIXTURES_DIR / "auth.json", FIXTURES_DIR / "articles.json"]

    def setUp(self):
        self.hello_world_obj = Article.objects.first()

    def test_article_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), 3)

    def test_article_published_count(self):
        qs = Article.objects.all().published()
        self.assertEqual(qs.count(), 1)

    def test_article_pending_publish_count(self):
        qs = Article.objects.pending()
        self.assertEqual(qs.count(), 1)

    def test_article_draft_count(self):
        qs = Article.objects.drafts()
        self.assertEqual(qs.count(), 1)

    def test_unique_slug_feature(self):
        title = self.hello_world_obj.title
        slug = self.hello_world_obj.slug
        num_objs = 10
        new_obj = None
        for i in range(num_objs):
            _obj = Article.objects.create(title=title)
            if new_obj is None and (num_objs - 1 == i):
                new_obj = _obj
        self.assertNotEqual(new_obj.slug, slug)
        qs = Article.objects.filter(slug__iexact=slug)
        self.assertEqual(qs.count(), 1)
