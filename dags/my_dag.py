# from datetime import datetime, timedelta

# from airflow.models.dag import DAG
# from airflow.providers.papermill.operators.papermill import PapermillOperator


# with DAG(
#     dag_id='example_papermill_operator',
#     default_args={
#         'retries': 0
#     },
#     schedule='0 * * * *',
#     start_date=datetime(2022, 10, 1),
#     template_searchpath='/usr/local/airflow/dags',
#     catchup=False
# ) as dag_1:

#     notebook_task = PapermillOperator(
#         task_id="run_example_notebook",
#         input_nb="dags/allogisticompiler.ipynb",
#         output_nb="dags/out-{{ execution_date }}.ipynb",
#         parameters={"execution_date": "{{ execution_date }}"},
#     )






import pyautogui
import time

# Make sure you want to run an infinite loop
try:
    while True:
        # Get the screen size
        width, height = pyautogui.size()

        # Move the mouse to a random position within the screen bounds
        pyautogui.moveTo(width // 2, height // 2, duration=0.5)
        pyautogui.moveTo(width // 4, height // 4, duration=0.5)
        pyautogui.moveTo(3 * width // 4, 3 * height // 4, duration=0.5)
        pyautogui.moveTo(width // 2, height // 2, duration=0.5)

        # Sleep for a short period to make the movement visible and prevent high CPU usage
        time.sleep(1)

except KeyboardInterrupt:
    print("Mouse movement stopped.")
