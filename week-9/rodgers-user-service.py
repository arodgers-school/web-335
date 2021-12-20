# Adam Rodgers
# WEB335
# Assignment 9.2
# 12/19/2021

# Import statements
from pymongo import MongoClient
import pprint
import datetime

# Set MongoDB connection info
client = MongoClient('localhost', 27017)

# Specify database and build new user document
db = client.web335
user = {
    "first_name": "Adam",
    "last_name": "Rodgers",
    "email": "adrodgers@my365.bellevue.edu",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()
}

# Insert user document and return user_id
user_id = db.users.insert_one(user).inserted_id

# Print user_id
print(user_id)

# Specify employee_id to search for
employee_id = "0000008"

# Print document for specified employee ID
pprint.pprint(db.users.find_one({"employee_id": employee_id}))