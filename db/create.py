from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///database.db', echo = True)
meta = MetaData()

students = Table(
   'user', meta, 
   Column('id', Integer, primary_key = True), 
   Column('username', String), 
   Column('email', String, unique=True),
   Column('password', String),
)

meta.create_all(engine)