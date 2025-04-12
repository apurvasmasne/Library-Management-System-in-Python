# app.py
from library import add_author, add_book, add_member, borrow_book, return_book

def main():
    while True:
        print("Library Management System")
        print("1. Add Author")
        print("2. Add Book")
        print("3. Add Member")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter author name: ")
            birth_year = int(input("Enter birth year: "))
            country = input("Enter country: ")
            add_author(name, birth_year, country)
            print("Author added successfully!")
        
        elif choice == "2":
            title = input("Enter book title: ")
            author_id = int(input("Enter author ID: "))
            published_year = int(input("Enter published year: "))
            genre = input("Enter genre: ")
            available_quantity = int(input("Enter available quantity: "))
            add_book(title, author_id, published_year, genre, available_quantity)
            print("Book added successfully!")
        
        elif choice == "3":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            phone_number = input("Enter phone number: ")
            join_date = input("Enter join date (YYYY-MM-DD): ")
            add_member(name, email, phone_number, join_date)
            print("Member added successfully!")

        elif choice == "4":
            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))
            borrow_date = input("Enter borrow date (YYYY-MM-DD): ")
            borrow_book(member_id, book_id, borrow_date)
            print("Book borrowed successfully!")

        elif choice == "5":
            transaction_id = int(input("Enter transaction ID: "))
            return_date = input("Enter return date (YYYY-MM-DD): ")
            return_book(transaction_id, return_date)
            print("Book returned successfully!")

        elif choice == "6":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
