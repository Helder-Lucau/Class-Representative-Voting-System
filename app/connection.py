from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///voting.db")
Session = sessionmaker(bind=engine)
session = Session()

# create the base declarative class model
Base = declarative_base()