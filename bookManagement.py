import main
import menu as m
import json
import csv
import helper.read as r

books_csv = "csv/books.csv"



def bookManagement():
    print("Book Management")
    while True:
        print("""
[1] Add Book
[2] Remove Book
[3] Modify Book Details 
[0] Exit to Staff Menu
            """)
        try: 
            choice = int(input("Please Enter a Selection : ").strip())
            match choice:
                case 1 : addBook(); break
                case 2 : removeBook(); break
                case 3 : modifyBook(); break
                case 0 : main.clear(); m.staffMenu(); break
        except ValueError:
            main.clear(); print("Invalid input. Please enter a number.")

def addBook():
    title = input("Enter book title : ").strip()
    author = input("Enter author name : ").strip()
    isbn = input("Enter ISBN : ").strip()
    quantity = input("Enter Quantity : ").strip()

    books = r.readBook()
    
    if books:
        maxID = max(int(row[0][1:]) for row in books if row and row[0].startswith("B"))
        newID = f'B{maxID + 1:03d}'
    else:
        newID = 'B001'
    
    newBook = f"{newID},{title},{author},{isbn},{quantity},0"

    books.append(newBook)

    with open(books_csv, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(newBook)

    print(f"Book added successfully with ID {newID}!")
    input("Press Enter to return to Staff Menu...")
    main.clear(); m.staffMenu(); 

def removeBook():
    bookID = input("Enter the Book ID to remove ( e.g B001 ): ").strip().upper()
    try:
        with open('json/books.json', "r") as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        main.clear()
        print("No book with this ID found.")
        m.staffMenu()
        return
    
    newBooks = [book for book in books if book.get("book_id") != bookID]

    if len(newBooks) == len(books):
        print(f"No book found with ID {bookID}.")
    else:
        with open('json/books.json', "w") as file:
            json.dump(newBooks, file, indent=2)
        print(f"Book with ID {bookID}, removed successfully.")

    input("Press Enter to return to Staff Menu...")
    main.clear(); m.staffMenu(); 

def modifyBook():
    bookID = input("Enter the Book ID to edit (e.g. B001) : ").strip().upper()
    try:
        with open('json/books.json', 'r') as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No books found.")
        main.clear(); m.staffMenu()
        return

    for book in books:
        if book.get("book_id") == bookID:
            print(f"Editing book: {book['title']} by {book['author']}")
            print("Leave blank to keep current value.")
            new_title = input(f"New title [{book['title']}]: ").strip()
            new_author = input(f"New author [{book['author']}]: ").strip()
            new_isbn = input(f"New ISBN [{book['isbn']}]: ").strip()
            try:
                new_quantity = input(f"New quantity [{book['quantity']}]: ").strip()
                new_quantity = int(new_quantity) if new_quantity else book['quantity']
            except ValueError:
                print("Invalid quantity. Keeping previous value.")
                new_quantity = book['quantity']

            book['title'] = new_title if new_title else book['title']
            book['author'] = new_author if new_author else book['author']
            book['isbn'] = new_isbn if new_isbn else book['isbn']
            book['quantity'] = new_quantity

            with open('json/books.json', 'w') as file:
                json.dump(books, file, indent=2)

            print("Book details updated successfully.")
            input("Press Enter to return to Staff Menu...")
            main.clear(); m.staffMenu()
            return

    print(f"No book found with ID {bookID}.")
    input("Press Enter to return to Staff Menu...")
    main.clear(); m.staffMenu()

