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
    print('1 - View Issues | 2 - Create Issue | 3 - Exit')
    while running:
        user_input = input('Command: ')
        match user_input:
            case '1':
                get_issue_project = input('Project: ')
                get_issues(get_issue_project)
            case '2':
                new_issue_name = input('Name: ')
                new_issue_date = input('Due: ')
                new_issue_project = input('Project: ')
                new_issue(new_issue_name, new_issue_date, new_issue_project)
            case '3':
                running = False
                print('Bye')

    try:
        new_issue('Test3', '19/08/2022', 'Issue_Tracker')
    except Exception as ex:
        print("Error: ", ex)

