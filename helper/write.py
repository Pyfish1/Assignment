import csv
import read as r

users_csv = "csv/users.csv"
borrowed_csv = "csv/borrowed.csv"


def writeUser(id, content): # Overrides whole row
    index = 0 if int(id[1:]) <= 0 else int(id[1:]) - 1
    with open(users_csv, 'r', newline='') as file:
        rows = list(csv.reader(file))
    while len(rows) <= index:
        rows.append([])
    rows[index] = content

    with open(users_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def writeName(id, name): content = r.readUser(id); content[1] = name; writeUser(id, content)
def writeEmail(id, email): content = r.readUser(id); content[2] = email; writeUser(id, content)
def writePassword(id, password): content = r.readUser(id); content[4] = password; writeUser(id, content)
def writeAdminStatus(id, status): content = r.readUser(id); content[5] = status; writeUser(id, content)

def appendBooksToUser(id, bookID):
    borrowed_books, rows = r.read(id)

    if bookID in borrowed_books:
        print("Book already present")
        borrowed_books = borrowed_books # No changes
    else: # BookID is not present in borrowed_books
        borrowed_books.append(bookID)
    try:
        with open(borrowed_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except FileNotFoundError:
        print("File not found")

def removeBooksFromUser(id, bookID):
    borrowed_books, rows = r.read(id)
    
    if bookID not in borrowed_books:
        print("User does not have this book")
        borrowed_books = borrowed_books # No changes
    else:
        borrowed_books.remove(bookID)
    
    with open(borrowed_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

