from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from beginner_data_project.scripts.user_scripts import (
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
        dag=dag,
        task_id="extract_user_purchase_data",
        postgres_conn_id="postgres_default",
        sql="../scripts/sql/extract_user_purchase_data.sql",
        params={},
    )

    move_user_purchase_data_to_stage_data_lake = PythonOperator(
        dag=dag,
        task_id="move_user_purchase_data_to_stage_data_lake",
        python_callable=local_to_s3,
        op_kwargs={},
    )

    # make redshift aware of partition with redshift spectrum
    move_user_purchase_data_to_stage_data_lake_tbl = PythonOperator(
        dag=dag,
        task_id="move_user_purchase_data_to_stage_data_lake_tbl",
        python_callable=redshift_external_query,
        op_kwargs={},
    )

    (
        extract_user_purchase_data
        >> move_user_purchase_data_to_stage_data_lake
        >> move_user_purchase_data_to_stage_data_lake_tbl
    )
