from book import Book
from member import Member
from library_service import LibraryService
from exceptions import *

library = LibraryService()

while True:

    print("LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")

    choice = input("Choose an option: ")

    try:
        if choice not in ["1","2","3","4","5","6","7","8"]:
                raise InvalidMenuChoiceError("Invalid menu input.")
        
        if choice == "1":
            book = Book(
                input("Book ID: "),
                input("Title: "),
                input("Author: ")
            )
            library.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            member = Member(
                input("Member ID: "),
                input("Name: "),
                input("Email: ")
            )
            library.add_member(member)
            print("Member added successfully!")

        elif choice == "3":
            result = library.borrow_book(
                input("Book ID: "),
                input("Member ID: ")
            )
            print(result)

        elif choice == "4":
            result = library.return_book(input("Book ID: "))
            print(result)

        elif choice == "5":
            library.display_books()

        elif choice == "6":
            library.display_members()

        elif choice == "7":
            library.display_loans()

        elif choice == "8":
            print("Program ended.")
            exit() 

        else:
            print("Invalid option. Try again.")

    except BookNotFoundError as e:
        print("Error:", e)

    except MemberNotFoundError as e:
        print("Error:", e)

    except BookUnavailableError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected error:", e)