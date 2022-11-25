from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import text

engine = create_engine('sqlite:///database.db', echo = True)
meta = MetaData()

tq = text("""SELECT * FROM user""")
conn = engine.connect()
result = conn.execute(tq).fetchall()
print(result)