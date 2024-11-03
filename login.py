import os
import hashlib
import pickle
import proj.slowtype

# File to store user data
user= 'users.bin'

# Encrypts the password to make i unreadable]
def encrypter(password):
    return hashlib.sha256(password.encode()).hexdigest()


def initialize_users():
    if not os.path.exists(user):
        with open(user, 'wb') as file:
            pickle.dump({}, file) 

def load_users():
    with open(user, 'rb') as file:
        return pickle.load(file)

# Function to save user data to binary file
def register(user):
    with open(user, 'wb') as file:
        pickle.dump(users, file)

def signup():
    users = load_users()
    while True:
        username  = input('Username :')
        password  = input('Password :')
        
        if username in users:
            print("Username already exists. Please choose a different username.")
            continue
               
        pswd = pswd(password)
        
        users[username] = pswd
        register(users)
        
        print(f"User '{username}' registered successfully!")
        login()
        break
    
def login(username, password):
    users = load_users()
    username = input('Username :')
    password = input('Password :')

    
    if username not in users:
        print("Username does not exist. Please sign up first.")
        return 1
        # make it go back to main login/signup main menu
        
    pswd = pswd(password)
    if users[username] == pswd:
        print(f"Welcome back, {username}!")
        return True
    else:
        print("Incorrect password.")
        return False
