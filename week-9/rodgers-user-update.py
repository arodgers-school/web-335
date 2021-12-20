# Adam Rodgers
# WEB335
# Assignment 9.3
# 12/19/2021

# Import statements
from pymongo import MongoClient
import pprint
import datetime

# Set MongoDB connection info
client = MongoClient('localhost', 27017)

# Specify database and build new user document
db = client.web335

# Update email address for employee
db.users.update_one(
    {"employee_id": "0000008"},
    {
        "$set": {
            "email": "adam@gmail.com"
        }
    }
)

# Specify employee_id to search for
employee_id = "0000008"

# Print document for specified employee ID
pprint.pprint(db.users.find_one({"employee_id": employee_id}))