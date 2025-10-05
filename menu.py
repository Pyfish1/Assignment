import main
import bookManagement as bm
import userManagement as um
import bookTransactions as bt
import bookBorrowing as bb
import viewingHistory as vh
import searchAndInquiry as sai


def staffMenu():
    while True:
        print("""
[1] Book Management
[2] User Management
[3] Book Transaction
[4] Search & Inquiry 
[5] Reporting
[6] Viewing History
[0] Exit to Main Menu
            """)
        try:
            selection = int(input("Please Enter a Selection : ").strip())
            match selection:
                case 1: main.clear(); bm.bookManagement(); break
                case 2: main.clear(); um.userManagement(); break
                case 3: main.clear(); bt.bookTransactions(); break
                case 4: main.clear(); sai.searchAndInquiry(); break
                case 5: main.clear(); reporting(); break
                case 6: main.clear(); vh.viewingHistory(); break
                case 0: main.clear(); mainMenu(); break
                case _: main.clear(); print("Invalid selection. Please try again.")
        except ValueError:
            main.clear(); print("Invalid input. Please enter a number.")

def memberMenu(user):
    while True:
        print("""
[1] Book Borrowing
[2] Search & Availability
[3] Information Display
[0] Exit to Main Menu
            """)
        try:
            selection = int(input("Please Enter a Selection : ").strip())
            match selection:
                case 1: main.clear(); bb.bookBorrowing(user); break
                case 2: main.clear(); searchAndAvailability(); break
                case 3: main.clear(); informationDisplay(); break
                case 0: main.clear(); mainMenu(); break
                case _: main.clear(); print("Invalid selection. Please try again.")
        except ValueError:
            main.clear(); print("Invalid input. Please enter a number.")


def searchAndInquiry():
    print("Search & Inquiry")

def reporting():
    print("Reporting")

def searchAndAvailability():
    print("Search & Availability")

def informationDisplay():
    print("Information Display")

def mainMenu():
    main.clear()
    main.main()

