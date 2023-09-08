from connection import *
from models import Voter, Candidate, Vote
from faker import Faker
import random


if __name__ == '__main__':

    Base.metadata.create_all(engine)

    # clear our database before each new seed 
    session.query(Voter).delete()
    session.query(Candidate).delete()
    session.query(Vote).delete()

    fake = Faker()

    courses = ['Software engineering', 'Cybersecurity', 'Data Science', 'Soft Skills']

    # generate random voters records
    voter_list = []
    for i in range(10):
        voter = Voter(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            phone = fake.msisdn(),
            course = random.choice(courses)
        )
        session.add(voter)
        session.commit()
        voter_list.append(voter)

    # generate random candidate records
    candidate_list = []
    for i in range(10):
        candidate = Candidate(
            f_name = fake.first_name(),
            l_name = fake.last_name(),
            phone_no = fake.msisdn(),
            department = random.choice(courses)
        )
        session.add(candidate)
        session.commit()
        candidate_list.append(candidate)
    
session.close()