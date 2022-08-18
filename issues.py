# Imports
import sys
import argparse

app_description = """
    This is a test and a placeholder.
"""

parser = argparse.ArgumentParser(description = app_description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('-n', '--new', help='Create a new issue.')
parser.add_argument('-l', '--list', help='List all issues')
args = parser.parse_args()
config = vars(args)

print(config)

# Get CLI Arguments
#flag = sys.argv[1]


"""
# Check incoming flags
if flag == '-n':
    print('Create New Issue')


def new_issue():
    new_issue_name = input('Name: ')
    new_issue_due = input('Due: ')
    new_issue_project = input('Project: ')
    new_issue_details = input('Details: ')
    # Add to Database
    # Log success/fail

def update_issue():

# TEST PRINTS
print(n)
"""
