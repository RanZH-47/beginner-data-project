import os

from airflow.providers.amazon.aws.hooks.s3 import S3Hook


def local_to_s3(
    file_name: str, bucket_name: str, key: str, clear_local: bool = False
) -> None:
    s3 = S3Hook()
    s3.load_file(filename=file_name, bucket_name=bucket_name, replace=True, key=key)
    if clear_local:
        if os.path.isfile(file_name):
            os.remove(file_name)


def redshift_external_query():
    pass
