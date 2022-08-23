#!/usr/bin/python3

#Imports
import sys
import argparse
from datetime import datetime, timedelta
from sqlalchemy import create_engine

parser = argparse.ArgumentParser(description='Task/Issue Tracker')

#parser.add_argument('task')
args = parser.parse_args()

# Database connection
eng = create_engine('postgresql://Slappie64:v2_3taP7_NuF8dCDxLq7v8CMhstQs7gN@db.bit.io/Slappie64/issue_tracker', isolation_level='AUTOCOMMIT')

# Class - Custom class for tasks and the relevant variables
class Task:
    def __init__(self, uid, name, due):
        self.uid = uid
        self.name = name
        self.due = due

    created = datetime.now()
    details = ''
    status = ''

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


def format_task_info(in_task):

    format_task = Task(in_task['uid'], in_task['name'], in_task['date'])
    #for i in in_task.keys():
    #    print(i, in_task[i])
    #print('-'*10)
    return format_task

def auto_increment():
    result = conn.execute("SELECT MAX(UID) FROM issues;")
    return result.fetchone()[0] + 1

# TEST TASKS

task01 = Task(1, 'test1', specific_time_days(3))
task02 = Task(2, 'test2', specific_time_hours(36))
task03 = Task(3, 'test3', next_week)

#format_task_info(task01)
#format_task_info(task02)
#format_task_info(task03)

if __name__ == '__main__':
    with eng.connect() as conn:
        task_list = conn.execute("SELECT * FROM issues;")
        for i in task_list:
            print(format_task_info(i).uid)
            print(format_task_info(i).name)
            print(format_task_info(i).due)
            print('-'*10)
