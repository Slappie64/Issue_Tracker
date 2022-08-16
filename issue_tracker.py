# Imports
from sqlalchemy import create_engine

# Connection to database BIT.IO
eng = create_engine('postgresql://Slappie64:v2_3tQZz_nUMRUk8r9BVqtfbZdcxtUGE@db.bit.io/Slappie64/issue_tracker', isolation_level='AUTOCOMMIT')

# With the connection open...
with eng.connect() as conn:
    result = conn.execute("SELECT 'Hello bit.io!';")
    print(result.first()[0])
