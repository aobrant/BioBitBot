import os
from datetime import datetime

import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from models import create_tables, Records

load_dotenv()
username = os.getenv("DB_USERNAME")
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
dbname = os.getenv('DB_NAME')
DSN = f'postgresql://{username}:{password}@{host}/{dbname}'
# DSN = f'postgresql://postgres:{password}@localhost:5432/biobitbot_db'
engine = create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def save_data(user_d, parameter_d, value_d, units_d):
    try:
        user = user_d
        date = datetime.now()
        parameter = parameter_d
        value = value_d
        units = units_d
        new_record = Records(user=user, date=date, parameter=parameter, value=value, units=units)
        session.add(new_record)
        session.commit()
    except SQLAlchemyError as e:
        print(f"Error while working with database: {e}")
    finally:
        session.close()

    return "ok"
