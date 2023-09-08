import click
from connection import *
from models import Voter, Candidate, Vote

@click.group()
def cli():
      pass

# method returning all voters registered
@cli.command()
def all_voters():
     "Show a list of all voters"
     for voter in session.query(Voter).distinct():
        click.echo(voter)

# method to add new candidate 
@cli.command()
@click.option("--f_name", prompt="Enter your first name")
@click.option("--l_name", prompt="Enter your last name")
@click.option("--phone_no", prompt="Enter your phone number")
@click.option("--department", prompt="Enter your course")
 
def add_candidates(f_name, l_name, phone_no, department):
        new_candidate = Candidate(
            f_name = f_name,
            l_name = l_name,
            phone_no = phone_no,
            department = department
        )
        session.add(new_candidate)
        session.commit()
        click.echo(f"Candidate {f_name} {l_name} added sucessfully")

@cli.command()
def show_candidates():
      "Show a list of all candidates"
      for candidate in session.query(Candidate).all():
        click.echo(candidate)

if __name__ == '__main__':
   cli()

