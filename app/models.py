from connection import *

Base = declarative_base()

class Voter(Base):
    __tablename__ = "voters"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    phone = Column(Integer()) 
    course = Column(String())

    def __repr__(self):
        return f"review{self.id}: " \
            + f"first_name = {self.first_name}, " \
            + f"last_name = {self.last_name}, " \
            + f"phone = {self.phone}, " \
            + f"course = {self.course}" 

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    course = Column(String())
    party = Column(String())

    def __repr__(self):
        return f"review{self.id}: " \
            + f"first_name = {self.first_name}, " \
            + f"last_name = {self.last_name}, " \
            + f"course = {self.course}, " \
            + f"party = {self.party}" 

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer(), primary_key=True)
    voter_id = Column(Integer(), ForeignKey('voters.id'))
    candidate_id = Column(Integer(), ForeignKey('canditates.id'))
    vote_count = Column(Integer())

    def __repr__(self):
        return f"review{self.id}: " \
            + f"voter id = {self.voter_id}, " \
            + f"candidate id = {self.candidate_id}, " \
            + f"number of vote = {self.vote_count}" 