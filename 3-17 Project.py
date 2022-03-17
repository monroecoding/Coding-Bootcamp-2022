"""
Coding Bootcamp at the Monroe Township Library

3/17 Project

You'll be given a list of new employees at a restaurant and are tasked with creating a database that contains
each employee's name, an ID number, and a randomly assigned job
You'll need to create a dictionary for each employee containing three keys: name, ID, and job
Then add each dictionary to the database (which is a list)

Things to consider:
    -You can make your program easier/cleaner by using a loop
    -Assign an ID number however you want, but it should be in incremental integers (001, 002, 003, etc.)
    -Print out one of the items in the database list to make sure your program works as expected
"""

import random


employees = ["John", "Catherine", "Elisa"]
jobs = ["chef", "server", "custodian"]

database = []

#don't worry about understanding this yet, just use assign_job() when creating the job value for each person
#for example: {"job" : assign_job()}
def assign_job():
    """
    assigns a job randomly and updates the available jobs list
    """
    random.shuffle(jobs)
    job = jobs[0]
    jobs.remove(job)

    return job


#your code goes here