from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    dag_id="user_function",
    description="A pipeline to orchestrate data moving",
    schedule="0 0 * * *",
    catchup=False,
) as dag:
    None