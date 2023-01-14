import os

import psycopg2
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.postgres.hooks.postgres import PostgresHook


def local_to_s3(
    file_name: str, bucket_name: str, key: str, clear_local: bool = False
) -> None:
    s3 = S3Hook()
    s3.load_file(filename=file_name, bucket_name=bucket_name, replace=True, key=key)
    if clear_local:
        if os.path.isfile(file_name):
            os.remove(file_name)


def redshift_external_query(query: str) -> None:
    redshift_hook = PostgresHook(postgres_conn_id="redshift")
    redshift_conn = redshift_hook.get_conn()

    redshift_conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    redshift_cur = redshift_conn.cursor()
    redshift_cur.execute(query)
    redshift_conn.commit()
    redshift_cur.close()
    redshift_conn.close()
