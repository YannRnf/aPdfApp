from storages.backends.s3boto3 import S3Boto3Storage

# Storage class to specify the S3 bucket upload options and repository
class MediaStorage(S3Boto3Storage):
    location = 'privateMedia'
    default_acl = 'private'
    custom_domain = False
    file_overwrite = False