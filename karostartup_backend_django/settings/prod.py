from decouple import config

AWS_QUERYSTRING_AUTH = config("AWS_QUERYSTRING_AUTH", cast=bool)
AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_REGION = config("AWS_REGION")
SERVER_EMAIL = config("SERVER_EMAIL")
AWS_SNS_ENDPOINT = config("AWS_SNS_ENDPOINT")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "utils.s3_gateway.StaticStorage"
AWS_LOCATION = "static"
STATIC_URL = f"{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}"
