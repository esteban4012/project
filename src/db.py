from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from sqlalchemy.engine import URL

url_object = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="12345",  # plain (unescaped) text
    host="127.0.0.1",
    database="inventory",
)

engine = create_engine(url_object)
Session = sessionmaker(bind=engine)
session = Session()







class Base(DeclarativeBase):
    pass

