-- schema.sql
-- Create Database
CREATE DATABASE IF NOT EXISTS LibraryDB;

-- Use the created database
USE LibraryDB;

-- Create Authors Table
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    birth_year INT,
    country VARCHAR(50)
);

-- Create Books Table
CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    author_id INT,
    published_year INT,
    genre VARCHAR(50),
    available_quantity INT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- Create Members Table
CREATE TABLE IF NOT EXISTS Members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15),
    join_date DATE
);

-- Create Transactions Table
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    status ENUM('borrowed', 'returned') DEFAULT 'borrowed',
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
