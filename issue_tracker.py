# Imports
from sqlalchemy import create_engine

# Connection to database BIT.IO
eng = create_engine('postgresql://Slappie64:v2_3tQZz_nUMRUk8r9BVqtfbZdcxtUGE@db.bit.io/Slappie64/issue_tracker', isolation_level='AUTOCOMMIT')

# Automatically increment UID
def auto_increment():
    result = conn.execute("SELECT MAX(UID) FROM issues;")
    return result.fetchone()[0] + 1

# Create a new issue in the DB
def new_issue(name, date, project):
	conn.execute("INSERT INTO issues (UID, Name, Date, Project, Status) VALUES ('{}','{}','{}', '{}', 'Not Started');".format(auto_increment(), name, date, project))

# With the connection open...
with eng.connect() as conn:
    try:
        new_issue('Test3', '19/08/2022', 'Issue_Tracker')
    except Exception as ex:
        print("Error: ", ex)

