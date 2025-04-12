# library.py
from db_connection import create_connection

def add_author(name, birth_year, country):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Authors (name, birth_year, country) VALUES (%s, %s, %s)", (name, birth_year, country))
    connection.commit()
    cursor.close()
    connection.close()

def add_book(title, author_id, published_year, genre, available_quantity):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Books (title, author_id, published_year, genre, available_quantity) VALUES (%s, %s, %s, %s, %s)", 
                   (title, author_id, published_year, genre, available_quantity))
    connection.commit()
    cursor.close()
    connection.close()

def add_member(name, email, phone_number, join_date):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Members (name, email, phone_number, join_date) VALUES (%s, %s, %s, %s)", 
                   (name, email, phone_number, join_date))
    connection.commit()
    cursor.close()
    connection.close()

def borrow_book(member_id, book_id, borrow_date):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Transactions (member_id, book_id, borrow_date) VALUES (%s, %s, %s)", 
                   (member_id, book_id, borrow_date))
    cursor.execute("UPDATE Books SET available_quantity = available_quantity - 1 WHERE book_id = %s", (book_id,))
    connection.commit()
    cursor.close()
    connection.close()

def return_book(transaction_id, return_date):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Transactions SET return_date = %s, status = 'returned' WHERE transaction_id = %s", 
                   (return_date, transaction_id))
    cursor.execute("UPDATE Books SET available_quantity = available_quantity + 1 WHERE book_id = (SELECT book_id FROM Transactions WHERE transaction_id = %s)", (transaction_id,))
    connection.commit()
    cursor.close()
    connection.close()
