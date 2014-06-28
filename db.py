#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError

from settings import DB_URI


engine = create_engine(DB_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = scoped_session(Session)

Base = declarative_base()
Base.query = session.query_property()


if __name__ == '__main__':
    from models import *
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
