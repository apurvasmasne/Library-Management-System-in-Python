# db_connection.py
import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",        # your host
        user="root",             # your username
        password="password",     # your password
        database="LibraryDB"     # your database name
    )
    return connection
