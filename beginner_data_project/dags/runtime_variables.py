from airflow.models import Variable

bucket_name = Variable.get("BUCKET")
