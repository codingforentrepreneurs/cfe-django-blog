from storages.backends.s3boto3 import S3Boto3Storage

from . import mixins


class PublicS3Boto3Storage(mixins.DefaultACLMixin, S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class MediaS3BotoStorage(mixins.DefaultACLMixin, S3Boto3Storage):
    location = 'media'
    default_acl = 'private'
