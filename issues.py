# Imports
import sys
import argparse

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


#group.add_argument('-n', '--new', action='store', dest='issue_name', help='Create a new issue.')
#group.add_argument('-l', '--list', action='store_true', help='List all issues.')
#group.add_argument('-u', '--update', action='store', dest='issue_UID', help='Update issue, requires issue ID')


args = parser.parse_args()
config = vars(args)

arg_in = sys.argv[1]

match arg_in:
    case 'new':
        print('Create a new issue.')
    case 'list':
        print('List all issues.')
    case 'update':
        'Update an issue.'

# Function - Line breaks for testing
def line_break():
    print('-'*20)
    

# TEST PRINTS

print(vars(args))

line_break()

for i in config:
    print(i)

print(sys.argv[1])

