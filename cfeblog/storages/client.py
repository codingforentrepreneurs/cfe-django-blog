import boto3
from django.conf import settings

AWS_ACCESS_KEY_ID = getattr(settings, "AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = getattr(settings, 'AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = getattr(settings, 'AWS_S3_REGION_NAME')
AWS_STORAGE_BUCKET_NAME = getattr(settings, 'AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = getattr(settings, 'AWS_S3_ENDPOINT_URL')
def get_boto3_client(service='s3'):
    if not all([
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        AWS_S3_REGION_NAME,
        AWS_S3_ENDPOINT_URL
    ]):
        return None
    return boto3.client(service, 
                      aws_access_key_id=AWS_ACCESS_KEY_ID, 
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
                      region_name=AWS_S3_REGION_NAME,
                      endpoint_url = AWS_S3_ENDPOINT_URL
                      )
                      

def get_boto3_resource(service='s3'):
    if not all([
        AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY,
        AWS_S3_REGION_NAME,
        AWS_S3_ENDPOINT_URL
    ]):
        return None
    session = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY_ID, 
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
        region_name=AWS_S3_REGION_NAME,
   
    )
    return session.resource(service_name=service,
    endpoint_url=AWS_S3_ENDPOINT_URL,)


def get_storage_bucket(bucket_name=AWS_STORAGE_BUCKET_NAME):
    """
    Usage options:
    from cfeblog.storages import client

    my_bucket = client.get_storage_bucket()

    list objects:
    ```
    for file in my_bucket.objects.all():
        print(file.key)
    ```
    
    delete objects:
    ```
    my_bucket.objects.delete()
    ```
    """
    if not bucket_name:
        return None
    resource = get_boto3_resource(service='s3')
    if not resource:
        return None
    return resource.Bucket(bucket_name)



