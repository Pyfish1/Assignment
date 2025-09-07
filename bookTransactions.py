import json

import main
import menu as m
import datetime


def bookTransactions():
    print("Book Transactions")
    while True:
        print("""
[1] Issue Books to a Member
[2] Mark Books as Returned
[0] Exit to Staff Menu
        """)

        try:
            choice = int(input("Please Enter a Selection : ").strip())
            match choice:
                case 1 : issueBook(); break
                case 2 : returnBook(); break
                case 0 : main.clear(); m.staffMenu(); break
        except ValueError:
            main.clear(); print("Invalid input. PLease enter a number. ")
            input("Press Enter to Exit...")
            main.clear()
            m.memberMenu()


def issueBook():
    bookID = input("Please Enter the Book ID to issue (e.g B001) : ").strip().upper()
    userID = input("Please Enter the User ID to be issued to (e.g U001) : ").strip().upper()
    dueDate = (datetime.date.today() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")

    try:
        with open('json/books.json') as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No Books Found")
        main.clear(); m.staffMenu()
        return
    try:
        with open('json/users.json') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No Users Found")
        main.clear(); m.staffMenu()

    for book in books:
        if book['book_id'] == bookID : # We are now editing a specific book
            alreadyBorrowed = any(b['borrower_id'] == userID for b in book['borrowers'])
            if alreadyBorrowed:
                print("User has already borrowed this book.")
                input("Press Enter to continue...")
                main.clear(); m.staffMenu(); return

            available = book['quantity'] - book['quantity_borrowed']
            if available <= 0:
                print("No copies available for this book.")
                input("Press Enter to continue...")
                main.clear()
                m.staffMenu()
                return

            print(f"Issuing Book : {book['title']} by {book['author']}")
            book['quantity_borrowed'] += 1
            book['borrowers'].append({
                "borrower_id" : userID,
                "due_date" : dueDate,
            })
            for user in users:
                if user['user_id'] == userID:
                    print(f"Issuing to User : {user['name']} with ID {user['user_id']}")
                    user['borrowed_books'].append(bookID)

    with open('json/users.json', 'w') as file:
        json.dump(users, file)
    with open('json/books.json', 'w') as file:
        json.dump(books, file)

    print("Book Issued successfully.")
    input("Press Enter to return to Staff Menu...")
    main.clear(); m.staffMenu()
    return

def returnBook():
    bookID = input("Please Enter the Book ID to return (e.g B001) : ").strip().upper()
    userID = input("Please Enter the User ID who returned (e.g U001) : ").strip().upper()

    try:
        with open('json/books.json') as file:
            books = json.load(file)
        with open('json/users.json') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Books or Users file missing/corrupt")
        main.clear(); m.staffMenu()
        return

    for book in books:
        if book['book_id'] == bookID:
            print(f"Returning Book : {book['title']} by {book['author']}")
            book['borrowers'] = [b for b in book.get('borrowers', []) if b['borrower_id'] != userID]
            if book['quantity_borrowed'] > 0:
                book['quantity_borrowed'] -= 1
            break

    for user in users:
        if user['user_id'] == userID:
            print(f"Returning from User : {user['name']} with ID {user['user_id']}")
            if bookID in user.get('borrowed_books', []):
                user['borrowed_books'].remove(bookID)
            break

    with open('json/users.json', 'w') as file:
        json.dump(users, file, indent=4)
    with open('json/books.json', 'w') as file:
        json.dump(books, file, indent=4)

    print("Book Returned successfully.")
    input("Press Enter to return to Staff Menu...")
    main.clear(); m.staffMenu()


































