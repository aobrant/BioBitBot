import os
from datetime import datetime
from collections import defaultdict

import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, select, func, Column, String, Float
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


def count_items_for_user(user_name):
    res_dict = defaultdict(int)  # Используем defaultdict для автоматического создания счетчиков
    records = session.query(Records).filter(Records.user == user_name)
    for record in records:
        parameter = record.parameter
        res_dict[parameter] += 1

    return dict(res_dict)


def list_items_for_user(user_name):
    records = session.query(Records).filter(Records.user == user_name)
    unique_records = records.distinct(Records.parameter).all()
    unique_parameters = [record.parameter for record in unique_records]
    return unique_parameters


def list_rec_time(parameter):
    data = session.query(Records.date, Records.value, Records.units).filter(Records.parameter == parameter).all()
    dates = [row.date for row in data]
    values = [row.value for row in data]
    units = data[0].units
    return values, dates, units

