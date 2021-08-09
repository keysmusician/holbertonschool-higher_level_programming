#!/usr/bin/python3
"""Class definition of a `State`. Connect to a DB using SQL Alchemy."""
import sqlalchemy
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class corresponding to MySQL `states` table."""
    __tablename__ = "states"

    id = sqlalchemy.Column(
        Integer, unique=True, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(String(128), nullable=False)
