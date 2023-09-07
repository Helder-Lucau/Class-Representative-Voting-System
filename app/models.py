from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///elections.db')

Base = declarative_base()

class Voter(Base):
    __tablename__ = "voters"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    phone = Column(Integer) 
    course = Column(String()) 

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    course = Column(String())
    party = Column(String())

class Votes(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True)
    voter_id = Column(Integer, ForeignKey('voters.id'))
    candidate_id = Column(Integer, ForeignKey('canditates.id'))

    