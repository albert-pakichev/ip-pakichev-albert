#соединение с бд

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users_table = Table('users', metadata,
   Column('id', Integer, primary_key=True),
   Column('name', String),
   Column('fullname', String),
   Column('password', String)
)
# Column('name', String(50))

metadata.create_all(engine)
#создание сессий
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
#добавление новых элементов
