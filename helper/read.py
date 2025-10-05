import csv

users_csv = "csv/users.csv"
borrowed_csv = "csv/borrowed.csv"
books_csv = 'csv/books.csv'


def readUser(id="#"): # Return a list from userID
    try:
        with open(users_csv, 'r', newline='') as file:
            rows = list(csv.reader(file))
        if id != "#": 
            index = 0 if int(id[1:]) <= 0 else int(id[1:]) - 1
            while len(rows) <= index: 
                rows.append([])
            return rows[index]
        else: return [row for row in rows if row]  
    except FileNotFoundError:
        print("File not found")

def readBorrowed(id):
    try:
        with open(borrowed_csv, 'r', newline='') as file:
            rows = list(csv.reader(file))
        if id != "#": 
            index = 0 if int(id[1:]) <= 0 else int(id[1:]) - 1
            while len(rows) <= index: 
                rows.append([])
            return rows[index]
        else: return [row for row in rows if row]  
    except FileNotFoundError:
        print("File not found")

def readBook(id="#"):
    try:
        with open(books_csv, 'r', newline='') as file:
            rows = list(csv.reader(file))
        if id != "#": 
            index = 0 if int(id[1:]) <= 0 else int(id[1:]) - 1
            while len(rows) <= index: 
                rows.append([])
            return rows[index]
        else: return [row for row in rows if row]  
    except FileNotFoundError:
        print("File not found")

def getNameByID(id): list = readUser(id); return list[1] # returns string
def getEmailByID(id): list = readUser(id); return list[2] # returns string
def getPasswordByID(id): list = readUser(id); return list[3] # returns string
def getAdminStatusByID(id): list = readUser(id); return True if (list[4]) == "true" else False # returns bool
def getBorrowedBooksIDByID(id): list = readBorrowed(id); return list # returns list

def getName(user): return user[1]
def getEmail(user): return user[2]
def getPassword(user): return user[3]
def getAdminStatus(user): return True if (user[4]) == "true" else False
# def getBorrowed

