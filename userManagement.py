import main 
import menu as m
import json

def userManagement():
    print("User Management")
    while True:
        print("""
[1] Add User
[2] Remove User
[3] Modify User Details
[0] Exit to Staff Menu
            """)
        
        try:
            choice = int(input("Please Enter a Selection : ").strip())
            match choice:
                case 1 : addUser(); break
                case 2 : removeUser(); break
                case 3 : modifyUser(); break
                case 0 : main.clear(); m.staffMenu(); break
        except ValueError:
            main.clear(); print("Invalid input. Please enter a number.")

def addUser():
    name = input("Enter User Name : ").strip()
    email = input("Enter User Email : ").strip()
    password = input("Enter User Password : ").strip()
    admin = input("Enter Admin Status [Y/N] : ")

    try:
        with open('json/users.json', 'r') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []
    
    if users:
        maxID = max(int(user['user_id'][1:]) for user in users if user.get("user_id", "").startswith("U"))
        newID = f'U{maxID + 1:03d}'
    else:
        newID = 'U001'
    
    newUser = {
        "user_id" : newID,
        "name" : name,
        "email" : email, 
        "borrowed_books" : [],
        "password" : password,
        "admin" : True if admin.lower() == "Y" else False
    }

    users.append(newUser)
    with open('json/users.json', 'w') as file:
        json.dump(users, file, indent=0)
    
    print(f'User added Successfully with ID {newID}')
    input("Press Enter to return to Staff Menu...")
    main.clear(); m.staffMenu(); 

def removeUser():
    userID = input("Enter the User ID : ").strip().upper()
    try:
        with open('json/users.json', 'r') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        main.clear()
        print("No User with this ID found.")
        m.staffMenu()
        return
    
    newUsers = [user for user in users if user.get('user_id') != userID]
    if len(newUsers) == len(users):
        print(f"No user found with ID {userID}.")
    else:
        with open('json/users.json', "w") as file:
            json.dump(newUsers, file)
        print(f"User with ID {userID}, removed successfully.")
    
    input("Press Enter to return to Staff Menu...")
    main.clear(); m.staffMenu(); 

def modifyUser():
    userID = input("Enter the User ID to edit (e.g U001) : ").strip().upper()
    try: 
        with open('json/users.json', 'r') as file :
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No users found.")
        main.clear(); m.staffMenu()
        return
    
    for user in users:
        if user.get("user_id") == userID:
            print(f"Editing user: {user['name']} with ID {user['user_id']}")
            print("Leave black to keep current value.")
            newName = input(f"New Name [{user['name']}] : ").strip()
            newEmail = input(f"New Email [{user['email']}] : ").strip()
            newPassword = input(f"New Password [{user['password']}] : ").strip()
            newAdmin = True if input(f"New Admin Status [{user['admin']}] [Y/N] : ").lower() == 'Y' else False
            
            user['name'] = newName if newName else user['name']
            user['email'] = newEmail if newEmail else user['email'] 
            user['password'] = newPassword if newPassword else user['password']
            user['admin'] = newAdmin if newAdmin else user['admin']

            with open('json/users.json', 'w') as file:
                json.dump(users, file)
            
            print("User details updated successfully.")
            input("Press Enter to return to Staff Menu...")
            main.clear(); m.staffMenu()
            return
        
        print(f"No user found with ID {userID}")
        input("Press Enter to return to Staff Menu...")
        main.clear(); m.staffMenu()


