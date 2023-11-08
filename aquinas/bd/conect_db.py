import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
host = "mysql"
database = os.environ.get("MYSQL_DATABASE")
DATABASE_URL = f"mysql+mysqlconnector://{user}:{password}@{host}:3306/{database}" # noqa

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
