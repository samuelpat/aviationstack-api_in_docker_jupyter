from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from src.getFlightData import flow_getApiData
from src.transformFlightsData import flow_transformApiData
from src.loadTable import flow_loadApiData


import requests
import json
import os


# Define the default dag arguments.
default_args = {
    'owner': 'Samuel Patiño'
    #'depends_on_past': False,
    #'email': ['aditya.satrya@gmail.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    #'retries': 5,
    #'retry_delay': timedelta(minutes=1)
}


# Define the dag, the start date and how frequently it runs.
# I chose the dag to run everday by using 1440 minutes.
dag = DAG(
    dag_id='flightDag',
    default_args=default_args,
    start_date=datetime(2021, 1, 1),
    #schedule_interval=timedelta(minutes=1440)
    )


# First task is to query get the weather from openweathermap.org.
task1 = PythonOperator(
    task_id='get_apiData',
    #provide_context=True,
    python_callable=flow_getApiData,
    dag=dag
    )


# Second task is to transform the data
task2 = PythonOperator(
    task_id='transform_apiData',
    #provide_context=True,
    python_callable=flow_transformApiData,
    dag=dag
    )

# Third task is to load data into the database.
task3 = PythonOperator(
    task_id='load_apiData',
    #provide_context=True,
    python_callable=flow_loadApiData,
    dag=dag
    )

# Set task1 "upstream" of task2
# task1 must be completed before task2 can be started
task1 >> task2 >> task3
