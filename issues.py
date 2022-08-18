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
#new_parser.add_argument('-test', action='store_true')
new_parser.add_argument('-n', '--name', action='store', dest='issue_name', help='New Issue Name.')
new_parser.add_argument('-d', '--due', action='store', dest='issue_due', help='New Issue Due Date.')

# UPDATE - Sub Arguments for the UPDATE command.
update_parser = subparsers.add_parser('update', help='Update an exisiting issue.')
update_parser.add_argument('-uid', action='store', dest='issue_uid', help='UID of issue to update.')

# LIST - Sub Arguments for the LIST command.
list_parser = subparsers.add_parser('list', help='List issues.')
list_parser.add_argument('-p', '--project', action='store', dest='issue_project', help='Filter by project.')
list_parser.add_argument('-d', '--due', action='store', dest='issue_due', help='Filter by due date.')


args = parser.parse_args()
config = vars(args)

arg_in = sys.argv[1]

# Database connection
eng = create_engine('postgresql://Slappie64:v2_3tQZz_nUMRUk8r9BVqtfbZdcxtUGE@db.bit.io/Slappie64/issue_tracker', isolation_level='AUTOCOMMIT')



# Function - Add Issue to database
def new_issue():
    return 'new issue'

# Function - List Issues
def list_issues():
    return 'list issues'

def update_issue():
    return 'update issue'

# Function - Check for which argument was given
def get_arg_input(input):
    match input:
        case 'new':
            print('Create a new issue.')
        case 'list':
            if config['issue_project'] != None and config['issue_due'] != None:
                print('List all issues in project {}, that are due {}'.format(config['issue_project'], check_date_format(config['issue_due'])))
            elif config['issue_project'] != None:
                print('List all issues in project {}.'.format(config['issue_project']))
            elif config['issue_due'] != None:
                print('list all issues due {}.'.format(check_date_format(config['issue_due'])))
            else:
                print('List all issues.')
        case 'update':
            'Update an issue.'

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
    get_arg_input(arg_in)

    # Test Prints
    for i in config:
        print(i)

