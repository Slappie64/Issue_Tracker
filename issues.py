#!/usr/bin/python3

# Imports
import sys
import argparse
from sqlalchemy import create_engine

app_description = """
    This is a test and a placeholder.
"""

parser = argparse.ArgumentParser(description = app_description, prog='Issue Tracker')

#group = parser.add_mutually_exclusive_group()


# Create a subparsers parser
subparsers = parser.add_subparsers()

# NEW - Sub Arguments for the NEW command.
new_parser = subparsers.add_parser('new', help='Create a new issue.')
new_parser.add_argument('-n', '--name', action='store', dest='issue_name', help='New Issue Name.')
new_parser.add_argument('-d', '--due', action='store', dest='issue_due', help='New Issue Due Date.')
new_parser.add_argument('-p', '--project', action='store', dest='issue_project', help='New Issue Project')

# UPDATE - Sub Arguments for the UPDATE command.
update_parser = subparsers.add_parser('update', help='Update an exisiting issue.')
update_parser.add_argument('uid', help='UID of issue to update.')
update_parser.add_argument('-n', '--name', action='store', dest='issue_name', help='Update Issue Name')

# LIST - Sub Arguments for the LIST command.
list_parser = subparsers.add_parser('list', help='List issues.')
list_parser.add_argument('-a', '--all', action='store_true', dest='issue_all', help='Get all issues')
list_parser.add_argument('-p', '--project', action='store', dest='issue_project', help='Filter by project.')
list_parser.add_argument('-d', '--due', action='store', dest='issue_due', help='Filter by due date.')

# FIND - Sub Arguments for the FIND command
list_parser = subparsers.add_parser('find', help='Find specific Issues.')
list_parser.add_argument('name', help='Get UID by name')

args = parser.parse_args()
config = vars(args)

arg_in = sys.argv[1]

# Database connection
eng = create_engine('postgresql://Slappie64:v2_3tQZz_nUMRUk8r9BVqtfbZdcxtUGE@db.bit.io/Slappie64/issue_tracker', isolation_level='AUTOCOMMIT')

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

# Function - Format readble output
def format_output(issue_in):
    issue_out = ''
    for i in issue_in:
        issue_out += str(i)
        issue_out += " | "
        if 'Overdue' in issue_out:
            issue_out = bcolours.FAIL + issue_out
        elif 'In Progress' in issue_out:
            issue_out = bcolours.OKGREEN + issue_out
        elif 'Not Started' in issue_out:
            issue_out = bcolours.WARNING + issue_out
    return issue_out

# Function - Search for UID
def find_issue(name):
    result = conn.execute("SELECT * FROM issues WHERE name='{}';".format(name))
    return result.fetchone()[0]

# Function - Get highest UID from Database and increment
def auto_increment():
    result = conn.execute("SELECT MAX(UID) FROM issues;")
    return result.fetchone()[0] + 1

# Function - Add Issue to database
def new_issue(name, due='', project=''):
    conn.execute("INSERT INTO issues (UID, Name, Date, Project, Status) VALUES ('{}', '{}', '{}', '{}', 'Not Started');".format(auto_increment(), name, due, project))

# Function - List Issues
def list_issues(all_issues = False, due='', project=''):
    if all_issues == True:
        result = conn.execute("SELECT * FROM issues")
    else:
        if due != None and project != None:
            result = conn.execute("SELECT * FROM issues WHERE date='{}' AND project='{}';".format(due, project))
        else:
            result = conn.execute("SELECT * FROM issues WHERE date='{}' OR project='{}';".format(due, project))
    for i in result:
        print(format_output(i))

# Function - Update an existing issue
def update_issue(uid):
    update_issue_dict = {'name': '', 'date':'', 'project':'', 'status':'', 'details':''}
    update_issue_dict['name'] = input('Name: ')
    update_issue_dict['date'] = input('Due Date: ')
    update_issue_dict['project'] = input('Project: ')
    update_issue_dict['status'] = input('Status: ')
    update_issue_dict['details'] = input('Details: ')

    for key, value in update_issue_dict.items():
        if value == '':
            continue
        else:
            conn.execute("UPDATE issues SET {} = '{}' WHERE uid = {};".format(key, value, uid))
    return uid

# Function - Check for which argument was given
def get_arg_input(input):
    match input:
        case 'new':
            print('Create a new issue.')
            new_issue(config['issue_name'], config['issue_due'], config['issue_project'])
            print('Successully created issue {}.'.format(config['issue_name']))
        case 'list':
            list_issues(config['issue_all'], config['issue_due'], config['issue_project'])
        case 'update':
            print(update_issue(config['uid']))
        case 'find':
            print(find_issue(config['name']))

# Function - Line breaks for testing
def line_break():
    print('-'*20)

# Function - Check date formatting
def check_date_format(date_string):
    if '/' in date_string:
        return('on ' + date_string)
    else:
        return date_string
    

if __name__ == '__main__':
    with eng.connect() as conn:
        get_arg_input(arg_in)


    #Test Prints
    for i in config:
        print(i, config[i])

