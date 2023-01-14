from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from beginner_data_project.dags.runtime_variables import bucket_name
from beginner_data_project.scripts.aws.user_scripts import (
    local_to_s3,
    redshift_external_query,
)

with DAG(
    dag_id="user_function",
    description="A pipeline to orchestrate data moving",
    schedule="0 0 * * *",
    catchup=False,
) as dag:
    extract_user_purchase_data = PostgresOperator(
        task_id="extract_user_purchase_data",
        postgres_conn_id="postgres_default",
        sql="./scripts/sql/extract_user_purchase_data.sql",
        params={"user_purchase": "/temp/user_purchase.csv"},
        depends_on_past=True,
        wait_for_downstream=True,
    )

    move_user_purchase_data_to_stage_data_lake = PythonOperator(
        task_id="move_user_purchase_data_to_stage_data_lake",
        python_callable=local_to_s3,
        op_kwargs={
            "file_name": "/opt/airflow/temp/user_purchase.csv",
            "bucket_name": bucket_name,
            "key": "stage/user_purchase/{{ ds }}/user_purchase.csv",
            "clear_local": "true",
        },
    )

    # make redshift aware of partition with redshift spectrum
    move_user_purchase_data_to_stage_data_lake_tbl = PythonOperator(
        task_id="move_user_purchase_data_to_stage_data_lake_tbl",
        python_callable=redshift_external_query,
        op_kwargs={
            "query": "ALTER TABLE spectrum.user_purchase_staging \
            ADD IF NOT EXISTS PARTITION(insert_date = '{{ ds }}')\
                LOCATION s3://"
            + bucket_name
            + "/stage/user_purchase/{{ ds }}"
        },
    )

    (
        extract_user_purchase_data
        >> move_user_purchase_data_to_stage_data_lake
        >> move_user_purchase_data_to_stage_data_lake_tbl
    )
