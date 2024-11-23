# secure_code_review.py
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch sensitive data from environment variables
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Simple authentication function (to demonstrate secure coding)
def authenticate(user_input, pass_input):
    if user_input == username and pass_input == password:
        print("Authentication Successful")
    else:
        print("Authentication Failed")

# Simulate user input for authentication
user_input = input("Enter username: ")
pass_input = input("Enter password: ")

authenticate(user_input, pass_input)
