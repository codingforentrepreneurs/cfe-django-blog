import pathlib
import random
import string
import uuid

from django.utils.text import slugify


def get_article_image_upload_to(instance, filename):
    fpath = pathlib.Path(filename)
    fname = f"{uuid.uuid1()}{fpath.suffix}"
    slug = instance.slug
    if not slug:
        if instance.title:
            temp_slug = unique_slug_generator(instance)
        else:
            temp_slug = random_string_generator(size=15)
        slug = temp_slug
    return f"articles/{slug}/{fname}"


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
    Reference post https://cfe.sh/blog/random-string-generator-in-python/
    """
    return "".join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    Reference post https://cfe.sh/blog/a-unique-slug-generator-for-django/
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
