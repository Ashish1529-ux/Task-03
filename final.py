import os
from dotenv import load_dotenv
import bcrypt
from getpass import getpass

# Load environment variables from .env file
load_dotenv()

# Get credentials securely from environment
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Store password securely (hashed and salted)
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode(), salt)
    return hashed_pw

# Verify password (check if the input password matches the hashed password)
def verify_password(stored_hash, input_pw):
    return bcrypt.checkpw(input_pw.encode(), stored_hash)

# Example usage
stored_hash = hash_password(password)  # Store the password securely in the database

# Simulate login
input_password = getpass(f"Enter password for {username}: ")
if verify_password(stored_hash, input_password):
    print("Login successful!")
else:
    print("Invalid password.")
