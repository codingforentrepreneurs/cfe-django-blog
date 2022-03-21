import os

DJANGO_STORAGE_SERVICE = os.environ.get("DJANGO_STORAGE_SERVICE")

if DJANGO_STORAGE_SERVICE is not None:
    """
    Set default options from django-storages 
    if DJANGO_STORAGE_SERVICE key exists
    """
    # USER UPLOADED MEDIA
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    # Staticfiles
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


if DJANGO_STORAGE_SERVICE == 'linode':
    from .services.linode import *  # noqa
