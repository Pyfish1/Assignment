import main
import menu as m
import datetime
import json

def bookBorrowing(user):
    print(user)
    print("Book Borrowing")
    while True:
        print("""
[1] Request to Borrow a Book
[2] Return a Book
[0] Exit to Member Menu
        """)

        try:
            choice = int(input("Please Enter a Selection : ").strip())
            match choice:
                case 1 : requestBook(user); break
                case 2 : memberReturnBook(user); break
                case 0 : main.clear(); m.memberMenu(user); break
        except ValueError:
            main.clear(); print("Invalid input. Please enter a number.")
            input("Press Enter to Exit...")
            main.clear()
            m.memberMenu(user)

def requestBook(user):
    bookID = input("Please Enter a Book ID to Request : ").strip().upper()
    userID = user['user_id']
    dueDate = (datetime.date.today() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")

    try:
        with open('json/books.json') as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No Books Found")
        main.clear(); m.memberMenu(user)
        return
    try:
        with open('json/users.json') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No Users Found")
        main.clear(); m.memberMenu(user)

    for book in books:
        if book['book_id'] == bookID :
            alreadyBorrowed = any(b['borrower_id'] == userID for b in book['borrowers'])
            if alreadyBorrowed:
                print("User has already borrowed this book.")
                input("Press Enter to continue...")
                main.clear(); m.memberMenu(user); return

            available = book['quantity'] - book['quantity_borrowed']
            if available <= 0:
                print("No copies available for this book.")
                input("Press Enter to continue...")
                main.clear()
                m.memberMenu(user)
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

    print("Book Issued successfully. Your Due Date is : " + dueDate)
    input("Press Enter to return to Member Menu...")
    main.clear(); m.memberMenu(user)
    return


def memberReturnBook(user):
    bookID = input("Please Enter the Book ID to return (e.g B001) : ").strip().upper()
    userID = user['user_id']

    try:
        with open('json/books.json') as file:
            books = json.load(file)
        with open('json/users.json') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Books or Users file missing/corrupt")
        main.clear(); m.memberMenu(user)
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
    input("Press Enter to return to Member Menu...")
    main.clear(); m.memberMenu(user)




