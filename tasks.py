#!/usr/bin/python3

#Imports
import sys
import argparse
from datetime import datetime, timedelta
from sqlalchemy import create_engine

parser = argparse.ArgumentParser(description='Task/Issue Tracker')

arg = sys.argv[1]
arg_value = sys.argv[2].lower()

parser.add_argument('-n', help='Create a new task.')
parser.add_argument('-l', help='List all tasks.')
parser.add_argument('-t', help='Testing purposes')
args = parser.parse_args()

# Database connection
eng = create_engine('postgresql://Slappie64:v2_3taP7_NuF8dCDxLq7v8CMhstQs7gN@db.bit.io/Slappie64/issue_tracker', isolation_level='AUTOCOMMIT')

# Class - Custom class for tasks and the relevant variables
class Task:
    def __init__(self, uid, name, date):
        self.uid = uid
        self.name = name
        self.date = date

    created = datetime.now()
    project = ''
    details = ''
    status = ''

# Class - Custom colours for output prompt
class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    STOP = '\033[0;0m'

# Time Deltas
today = datetime.now()
tomorrow = datetime.now() + timedelta(days=1)
next_week = datetime.now() + timedelta(days=7)

def specific_time_hours(amount):
    return datetime.now() + timedelta(hours=amount)
def specific_time_days(amount):
    return datetime.now() + timedelta(days=amount)
def specific_time_weeks(amount):
    return datetime.now() + timedelta(weeks=amount)


# Function - Format the dictionary returned from SQL Database into Task
def ftask(in_task):

    format_task = Task(in_task['uid'], in_task['name'], in_task['date'])
    format_task.details = in_task['project']
    #format_task.details = in_task['details']
    #format_task.status = in_task['status']
    return format_task

# Function - Get the highest number from the UID column and return MAX + 1
def auto_increment():

    result = conn.execute("SELECT MAX(UID) FROM issues;")
    return result.fetchone()[0] + 1

# Function - Report and format tasks
def task_report(task):
    print(bcolours.BOLD + 'UID: ' + str(task.uid) + bcolours.STOP)
    print(bcolours.OKCYAN + 'Name: ' + str(task.name) + bcolours.STOP)
    print('Due: ', task.date)
    print('Details: ', task.details)
    if task.status == 'Complete':
        print(bcolours.OKGREEN + 'Status: ', str(task.status) + bcolours.STOP)
    elif task.status == 'In Progress':
        print(bcolours.WARNING + 'Status: ' + str(task.status) + bcolours.STOP)
    else:
        print(bcolours.FAIL + 'Status: ' + str(task.status) + bcolours.STOP)
    print('Project: ', task.project)
    print('Created: ', task.created)
    print('-'*10)

# Function - Get arg input and match it to a case.
def get_arg(input):
    match input:
        case '-n':
            print('Create a new task called', arg_value)
        case '-l':
            if arg_value == 'all':
                task_list = conn.execute("SELECT * FROM issues;")
                for i in task_list:
                    task_report(ftask(i))
        case '-t':
            task_report(task01)

# TEST TASKS
task01 = Task(25, 'test2', specific_time_hours(36))
task01.status = 'Complete'
task01.project = 'Test Project'
task01.details = 'Here are some details for the task'

#format_task_info(task02)
#format_task_info(task03)

if __name__ == '__main__':
    
    with eng.connect() as conn:
        get_arg(arg)
    """
        print(ftask(task01).uid)
        print(ftask(task01).name)
        print(ftask(task01).date)
        print(ftask(task01).project)
        
        task_list = conn.execute("SELECT * FROM issues;")
        for i in task_list:
            print('UID: ', ftask(i).uid)
            print('Name: ', ftask(i).name)
            print('Due: ', ftask(i).due)
            print('Details: ', ftask(i).details)
            print('Status: ', ftask(i).status)
            print('Project: ', ftask(i).project)
            print('Created: ', ftask(i).created)
            print('-'*10)
    """
