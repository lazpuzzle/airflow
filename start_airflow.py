# import module
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetiem, timedelta
from airflow.utils.dates import days_ago

# Default Arguments
default_args = {
	"owner" : "User",
	"depends_on_past" : False, # run when past job end
	'start_date' : days_ago(0), # 0 today (start tomorrow), 1 yesterday (start today)
	'email' : ['airflow@exmple.com'],
	'email_on_failure': False,
	'email_on_retry' : False,
	'retries': 1,
	'retry_delay': timedelta(minutes=5),
	'schedule_interval': '@daily' # can use crond
}

# instantiate a dag
dag = DAG('sample', catchup=False, default_args=default_args)

# with DAG('sample', catchup=False, default_args=default_args):

# Tasks

# task 1 show date
t1 = BashOperator(
	task_id='print date',
	bash_command='date',
	dag=dag,
	)

# task 2 list file
t2 = BashOperator(
	task_id='list_file',
	bash_command='ls -l',
	dag=dag,
	)

# Setting up Dependencies
t1 >> t2