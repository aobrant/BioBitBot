import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Records(Base):
    __tablename__ = "records"

    id = sq.Column(sq.Integer, primary_key=True)
    user = sq.Column(sq.Integer)
    parameter = sq.Column(sq.String(length=40))
    value = sq.Column(sq.DECIMAL(precision=10, scale=2))
    units = sq.Column(sq.TEXT)
    date = sq.Column(sq.DATETIME)


def create_tables(engine):
    # delete all previous data
    # Base.metadata.drop_all(engine)
    # Make tables
    Base.metadata.create_all(engine)
