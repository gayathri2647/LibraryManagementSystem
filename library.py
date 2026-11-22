# Library Management System

# Book Details
book_name = "Python Programming"
author = "Guido van Rossum"
price = 450

# Display Book Details
print("===== LIBRARY MANAGEMENT SYSTEM =====")
print("\nBook Details")
print("------------------------------")
print("Book Name:", book_name)
print("Author:", author)
print("Price: Rs.", price)

# Book Issue Functionality
print("\n===== BOOK ISSUE DETAILS =====")

student_name = input("Enter Student Name: ")
issue_book = input("Enter Book Name to Issue: ")

# Issue Book
if issue_book.lower() == book_name.lower():
    print("\nBook Issued Successfully!")
    print("Student Name:", student_name)
    print("Issued Book:", book_name)
else:
    print("\nSorry! Book is not available in the library.")