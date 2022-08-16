# Imports
from sqlalchemy import create_engine

# Application Loop
running = True

# Connection to database BIT.IO
eng = create_engine('postgresql://Slappie64:v2_3tQZz_nUMRUk8r9BVqtfbZdcxtUGE@db.bit.io/Slappie64/issue_tracker', isolation_level='AUTOCOMMIT')

# Automatically increment UID
def auto_increment():
    result = conn.execute("SELECT MAX(UID) FROM issues;")
    return result.fetchone()[0] + 1

# Create a new issue in the DB
def new_issue(name, date, project):
	conn.execute("INSERT INTO issues (UID, Name, Date, Project, Status) VALUES ('{}','{}','{}', '{}', 'Not Started');".format(auto_increment(), name, date, project))

# Get all issues with a project modifier
def get_issues(project = ""):
    if project == "":
        result = conn.execute("SELECT * FROM issues;")
        for i in result:
            print(i)
    else:
        result = conn.execute("SELECT * FROM issues WHERE project='{}';".format(project))
        for i in result:
            print(i)

# With the connection open...
with eng.connect() as conn:
    while running:
        print('1 - View Issues | 2 - Manage Issues | 3 - Exit')
        user_input = input('Command: ')
        match user_input:
            case '1':
                print('\nPlease enter project name or RETURN for all projects.\n')
                get_issue_project = input('Project: ')
                get_issues(get_issue_project)
                print('\n')
                print('-'*50)
            case '2':
                print('1 - Create Issue | 2 - Update Issues | 3 - Delete Issues | 4 - Previous')
                sub_user_input = input('Command: ')
                match sub_user_input:
                    case '1':
                        print('\nCreating new issue.\n')
                        new_issue_name = input('Name: ')
                        new_issue_date = input('Due: ')
                        new_issue_project = input('Project: ')
                        new_issue(new_issue_name, new_issue_date, new_issue_project)
                        print('\n')
                        print('-'*50)
                    case '2':
                        user_input = 0
            case '3':
                running = False
                print('Bye')
            case '0':
                print('back?')

