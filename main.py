import os
import json
import menu as m

def loadUsers(file='json/users.json'):
    with open(file, 'r') as file:
        return json.load(file)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def login(users):
    clear()
    print("--- Fantastic Books Library Login ---")
    email = input("Please Enter your email : ").strip(); clear()
    password = input("Please Enter your password : ").strip(); clear()
    for user in users:
        if user["email"] == email and user["password"] == password:
            menu(user)
            return user
    print("Invalid ID or Password")
    input("Press Enter to try again...")
    return None

def menu(user):
    print(user) # debug message
    if user["admin"]:
        print(f"Welcome Administrator {user['name']}")
        m.staffMenu()
    else: 
        print(f"Welcome Member {user['name']}")
        m.memberMenu(user)



def main():
    users = loadUsers() 
    user = None 
    while not user: 
        user = login(users) 

if __name__ == '__main__':
    main()