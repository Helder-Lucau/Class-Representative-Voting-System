from sqlalchemy import Column, Integer, String, ForeignKey
from connection import Base

class Voter(Base):
    __tablename__ = "voters"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    phone = Column(Integer()) 
    course = Column(String())

    def __repr__(self):
        return f"{self.id}: " \
        + f"First Name: {self.first_name}, " \
        + f"Last Name: {self.last_name}, " \
        + f"Phone: {self.phone}, " \
        + f"Course: {self.course}" 

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer(), primary_key=True)
    f_name = Column(String(), nullable=False)
    l_name = Column(String(), nullable=False)
    phone_no = Column(Integer())
    department = Column(String())

    def __repr__(self):
        return f"{self.id}: " \
        + f"First Name: {self.f_name}, " \
        + f"Last Name: {self.l_name}, " \
        + f"Phone_no: {self.phone_no}, " \
        + f"Course: {self.department}" 

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer(), primary_key=True)
    voter_id = Column(Integer(), ForeignKey('voters.id'))
    candidate_id = Column(Integer(), ForeignKey('candidates.id'))
    vote_count = Column(Integer())

    def __repr__(self):
        return f"{self.id}: " \
        + f"voter id = {self.voter_id}, " \
        + f"candidate id = {self.candidate_id}, " \
        + f"number of vote = {self.vote_count}" 
    
    