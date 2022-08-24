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
parser.add_argument('-p', help='List all tasks by project.')
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
    format_task.project = in_task['project']
    format_task.details = in_task['details']
    format_task.status = in_task['status']
    return format_task

# Function - Get the highest number from the UID column and return MAX + 1
def auto_increment():

    result = conn.execute("SELECT MAX(UID) FROM issues;")
    return result.fetchone()[0] + 1

# Function - Report and format tasks
def task_report(task):
    print('-'*50)
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
    #print('Created: ', task.created)
    print('-'*50)

def get_task(search_col, search_param):
    task_list = conn.execute("SELECT * FROM issues WHERE {}='{}';".format(search_col, search_param))
    return task_list

def new_task(task_name):
    task_name = task_name.lower()
    task_due = input("Due date: ").lower()
    task_project = input("Enter project code or leave blank: ").lower()
    task_details = input("Project details: ")

    try:
        conn.execute("INSERT INTO issues (UID, Name, Date, Project, Status) VALUES ('{}', '{}', '{}', '{}', 'Not Started');".format(auto_increment(),task_name, task_due, task_project))
        print('SUCCESS')
    except Exception as ex:
        print('There was an error: ', ex)
# Function - Get arg input and match it to a case.
def get_arg(input):
    match input:
        case '-n':
            print('Create a new task called', arg_value)
            new_task(arg_value)
        case '-p':
            match arg_value:
                case 'all':
                    task_list = conn.execute("SELECT * FROM issues;")
                    for i in task_list:
                        task_report(ftask(i))
                case default:
                    for i in get_task('project', arg_value):
                        task_report(ftask(i))
        case '-t':
            try:
                result = conn.execute("SELECT * FROM issues WHERE uid={}".format(arg_value))
                task_report(result.fetchone())
            except Exception as ex:
                print('There was an error: ', ex)
                print('-'*50)

# TEST TASKS
task01 = Task(25, 'test2', specific_time_hours(36))
task01.status = 'Complete'
task01.project = 'Test Project'
task01.details = 'Here are some details for the task'


if __name__ == '__main__':
    
    with eng.connect() as conn:
        get_arg(arg)

