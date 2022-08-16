# Imports
from sqlalchemy import create_engine

# Connection to database BIT.IO
eng = create_engine('postgresql://Slappie64:v2_3tQZz_nUMRUk8r9BVqtfbZdcxtUGE@db.bit.io/Slappie64/issue_tracker', isolation_level='AUTOCOMMIT')

def new_issue(uid, name, date, project):
	conn.execute("INSERT INTO issues (UID, Name, Date, Project, Status) VALUES ('{}','{}','{}', '{}', 'Not Started');".format(uid, name, date, project))


# With the connection open...
with eng.connect() as conn:
    try:
        new_issue('1','Test', '17/08/2022', 'Issue_Tracker')
    except Exception as ex:
        print("Error: ", ex)

