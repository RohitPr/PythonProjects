from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.timezone import datetime
from spotify_etl import run_spotify_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 6, 6),
    'email': 'airflow@example.com',
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG('spotify_dag', default_args=default_args,
          description='Our Spotify DAG', schedule_interval=timedelta(days=1))

run_etl = PythonOperator(task_id="complete_spotify_etl",
                         python_callable=run_spotify_etl, dag=dag)

run_etl
