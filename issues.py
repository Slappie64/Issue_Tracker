# Imports
import sys
import argparse

app_description = """
    This is a test and a placeholder.
"""

parser = argparse.ArgumentParser(description = app_description, prog='Issue Tracker')

#group = parser.add_mutually_exclusive_group()

subparsers = parser.add_subparsers(help='New')

new_parser = subparsers.add_parser('new', help='Create a new issue.')
new_parser.add_argument('-n', '--name', action='store', dest='issue_name', help='New Issue Name.')
new_parser.add_argument('-d', '--due', action='store', dest='issue_due', help='New Issue Due Date.')

update_parser = subparsers.add_parser('update', help='Update an exisiting issue.')
update_parser.add_argument('-uid', action='store', dest='issue_uid', help='UID of issue to update.')


list_parser = subparsers.add_parser('list', help='List issues.')
list_parser.add_argument('-p', '--project', action='store', dest='issue_project', help='Filter by project.')
list_parser.add_argument('-d', '--due', action='store', dest='issue_due', help='Filter by due date.')


#group.add_argument('-n', '--new', action='store', dest='issue_name', help='Create a new issue.')
#group.add_argument('-l', '--list', action='store_true', help='List all issues.')
#group.add_argument('-u', '--update', action='store', dest='issue_UID', help='Update issue, requires issue ID')



args = parser.parse_args()
config = vars(args)

def line_break():
    print('-'*20)

"""
# TEST PRINTS
# print(n)
print(config)
print(args)
line_break()
print(subparsers)
line_break()
print(new_parser)
print(update_parser)
print(list_parser)

#print(subparsers)

for i in config:
    print(i)

"""
