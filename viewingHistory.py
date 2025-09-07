import json
import main
import menu as m

def viewingHistory():
    userID = input("Please Enter the User ID to check Viewing History (e.g U001) : ").strip().upper()
    try:
        with open('json/users.json') as file:
            users = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No Users found")
        main.clear(); m.staffMenu(); return

    try:
        with open('json/books.json') as file:
            books = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No Books found")
        main.clear(); m.staffMenu(); return


    user = next((u for u in users if u.get("user_id") == userID), None)
    if not user:
        print("User not found.")
        input("Press Enter to return...")
        main.clear(); m.staffMenu(); return

    borrowed = user.get("borrowed_books", [])
    if not borrowed:
        print(f"{user['name']} (ID: {user['user_id']}) has no borrowed books.")
    else:
        print(f"Borrowing history for {user['name']} (ID: {user['user_id']}):")
        for book_id in borrowed:
            book = next((b for b in books if b.get("book_id") == book_id), None)
            if book:
                borrower_entry = next(
                    (br for br in book.get("borrowers", []) if br["borrower_id"] == userID),
                    None
                )
                if borrower_entry:
                    due_date = borrower_entry["due_date"]
                    print(f"- {book['title']} by {book['author']} (Due: {due_date})")
                else:
                    print(f"- {book['title']} by {book['author']} (Due date not found)")
            else:
                print(f"- {book_id} (book record not found)")

    input("Press Enter to return...")
    main.clear(); m.staffMenu()
