#!/usr/bin/env python

import datetime

from sqlalchemy import func
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from db import Base


class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)

    invited_on = Column(DateTime)
    created_on = Column(DateTime, default=datetime.datetime.utcnow())
    updated_on = Column(DateTime, default=func.now(), onupdate=func.now())

    @property
    def position(self):
        return self.get_registered_before() + 1

    @property
    def invited(self):
        if self.invited_on:
            return True
        return False

    def get_registered_before(self):
        return self.query.filter(Registration.id < self.id, Registration.invited_on == None).count()

    def serialize(self):
        return {
            'email': self.email,
            'position': self.position,
            'waiting_before': self.get_registered_before(),
            'invited': self.invited,
            'created_on': self.created_on.isoformat(),
        }

