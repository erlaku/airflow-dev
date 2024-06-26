FROM apache/airflow:2.9.2

# USER root
# RUN pip install papermill
# USER airflow
# WORKDIR ${AIRFLOW_HOME}
# COPY ./dags ${AIRFLOW_HOME}/dags
# RUN chmod +x ${AIRFLOW_HOME}/entrypoint.sh
# ENTRYPOINT ["./entrypoint.sh"]

# COPY requirements.txt /requirements.txt

# RUN pip install --user --upgrade pip
RUN pip install papermill