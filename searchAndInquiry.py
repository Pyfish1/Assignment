
print("searchAndInquiry.py imported successfully")
import json
import main
import menu as m

def searchAndInquiry():
    while True:
        try:
            with open('json/books.json', 'r') as file:
                books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            books = []
            print('File not found')
            input("Press Enter to continue...")
            return

        try:
            with open('json/users.json', 'r') as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []
            print("Users not found")
            input("Press Enter to continue...")
            return

        user_lookup = {user['user_id']: user['name'] for user in users}

        print("Book Title".ljust(40) + "NO. Borrowed".ljust(20) + "Borrowers")
        print("-" * 100)
        for book in books:
                if book['quantity_borrowed'] > 0:
                    title = str(book['title'])
                    quantity_borrowed = str(book['quantity_borrowed'])
                    # Get all unique borrower names for a certain book
                    borrower_names = list({user_lookup.get(b['borrower_id'], "Unknown User ID") for b in book['borrowers']})
                    print(title.ljust(40) + quantity_borrowed.ljust(20) + ", ".join(borrower_names))
        print("-" * 100)
        input("Press Enter to Exit to Staff Menu...")
        main.clear(); m.staffMenu(); return
