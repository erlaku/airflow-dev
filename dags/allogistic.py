import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import papermill as pm


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'update_allogistic',
    default_args=default_args,
    description='A simple DAG to run a Jupyter notebook',
    schedule_interval=timedelta(hours=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
)


NOTEBOOK_PATH = os.path.join(os.path.dirname(__file__), 'allogisticompiler.ipynb')
OUTPUT_NOTEBOOK_PATH = os.path.join(os.path.dirname(__file__), 'output_notebook.ipynb')


def run_notebook():
    pm.execute_notebook(
        NOTEBOOK_PATH,
        OUTPUT_NOTEBOOK_PATH,
    )

run_notebook_task = PythonOperator(
    task_id='run_notebook',
    python_callable=run_notebook,
    dag=dag,
)


run_notebook_task
