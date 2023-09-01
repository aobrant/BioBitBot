import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import create_tables, Records

username = os.getenv.get('DB_USERNAME')
password = os.getenv.get('DB_PASSWORD')
host = os.getenv.get('DB_HOST')
dbname = os.getenv.get('DB_NAME')
DSN = f'postgresql://{username}:{password}@{host}/{dbname}'
engine = create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


session.close()