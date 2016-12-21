import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class AmityPersons(Base):
	"""Create people table
	"""
	__tablename__ = 'person'
	person_id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String, nullable=False)
	position = Column(String, nullable=False)


class AmityRooms(Base):
	"""Create the rooms table
	"""
	__tablename__ = 'room'
	room_id = Column(Integer, primary_key=True, nullable=False)
	name = Column(String(32), nullable=False)
	room_type = Column(String(32), nullable=False)


class OfficeAllocations(Base):
	"""Store office allocations"""
	__tablename__ = "office_allocations"
	id = Column(Integer, primary_key=True)
	room_name = Column(String(32), nullable=False)
	members = Column(String(250))


class LivingSpaceAllocations(Base):
	"""Store living space allocations"""
	__tablename__ = "livingspace_allocations"
	id = Column(Integer, primary_key=True)
	room_name = Column(String(32), nullable=False)
	members = Column(String(250))

class UnAllocated(Base):
	"""Store people who are not allocated"""
	__tablename__ = "un_allocated"
	id = Column(Integer, primary_key=True)
	name = Column(String(250))

class DatabaseCreator(object):
	"""Creates a db connection object"""
	def __init__(self, db_name='default_db'):
		self.db_name = db_name
		if self.db_name:
			self.db_name = db_name + '.sqlite'
		else:
			self.db_name = 'default_amity_db.sqlite'
		self.engine = create_engine('sqlite:///' + self.db_name)
		self.session = sessionmaker(bind=self.engine)()
		Base.metadata.create_all(self.engine)
