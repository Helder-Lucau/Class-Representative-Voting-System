from faker import Faker
from connection import *
import random
from models import Voter, Candidate, Vote

fake = Faker()

if __name__ == '__main__':

    session.query(Voter).delete()
    session.query(Candidate).delete()
    session.query(Vote).delete()