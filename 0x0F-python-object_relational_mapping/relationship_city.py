#!/usr/bin/python3
"""Class definition of a `City`."""
from relationship_state import Base
import sqlalchemy
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String


class City(Base):
    """Class corresponding to MySQL `cities` table."""
    __tablename__ = "cities"

    id = sqlalchemy.Column(
        Integer, unique=True, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(String(128), nullable=False)
    state_id = sqlalchemy.Column(
        Integer, ForeignKey("states.id"), nullable=False)
