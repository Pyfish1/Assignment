import csv
borrowed_path = "Test/csv/borrowed.csv"

def readBorrowed(id):
    index = 1 if int(id[1:]) == 0 else int(id[1:]) - 1 # Failsafe
    try:
        with open(borrowed_path, 'r', newline='') as file:
            rows = list(csv.reader(file))
        while len(rows) <= index: 
            rows.append([])
        return rows[index], rows
    except FileNotFoundError:
        print("File not found")

def append(id, bookID):
    borrowed_books, rows = read(id)

    if bookID in borrowed_books:
        print("Book already present")
        borrowed_books = borrowed_books # No changes
    else: # BookID is not present in borrowed_books
        borrowed_books.append(bookID)

    with open(borrowed_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

append("U001", "B004")

def remove(id, bookID):
    borrowed_books, rows = read(id)
    
    if bookID not in borrowed_books:
        print("User does not have this book")
        borrowed_books = borrowed_books # No changes
    else:
        borrowed_books.remove(bookID)
    
    
    with open(borrowed_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)