#!/usr/bin/python3
"""Class definition of a `City`."""
import sqlalchemy
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class corresponding to MySQL `cities` table."""
    __tablename__ = "cities"

    id = sqlalchemy.Column(
        Integer, unique=True, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(String(128), nullable=False)
    state_id = sqlalchemy.Column(
        Integer, ForeignKey("states.id"), nullable=False
    )
