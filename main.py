import os
import json
import menu as m
import helper.read as r

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def login(users):
    clear()
    print("--- Fantastic Books Library Login ---")
    email = input("Please Enter your email : ").strip(); clear()
    password = input("Please Enter your password : ").strip(); clear()
    for user in users: # Loop through every user
        if r.getEmail(user) == email and r.getPassword(user) == password:
            menu(user)
            return user
    print("Invalid ID or Password")
    input("Press Enter to try again...")
    return None

def menu(user):
    print(str(user) + " Debug message") # debug message
    if r.getAdminStatus(user):
        print(f"Welcome Administrator {r.getName(user)}")
        m.staffMenu()
    else: 
        print(f"Welcome Member {r.getName(user)}")
        m.memberMenu(user)



def main():
    users = r.readUser()
    user = None 
    while not user: 
        user = login(users) 

if __name__ == '__main__':
    main()