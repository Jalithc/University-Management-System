# University-Management-System

This project implements a simple University Management System with the following classes:

Person: A base class to represent a person with basic attributes like name, age, and contacts.
Student: A class that inherits from Person and represents a student. It includes additional attributes and methods specific to students.
Lecturer: A class that inherits from Person and represents a lecturer. It includes additional attributes and methods specific to lecturers.
Classes and Methods
Person Class
The Person class is the base class for both Student and Lecturer.

Attributes:
name (str): The name of the person.
age (int): The age of the person.
contacts (str): The contact information of the person.
Methods:
__init__(self, name, age, contacts): Initializes the Person with the given name, age, and contacts.
Student Class
The Student class inherits from Person and adds attributes and methods specific to students.

Attributes:
student_ID (str): The student's ID.
year_of_entry (int): The year the student entered the university.
enroll_modules (list): A list of modules the student is enrolled in.
borrowed_books (list): A list of books the student has borrowed.
Methods:
__init__(self, name, age, contacts, student_ID, year_of_entry): Initializes the Student with the given attributes.
enroll_module(self, module): Enrolls the student in a module.
borrow_book(self, book_title, due_date): Borrows a book for the student until the specified due date.
return_book(self, book_title): Returns a borrowed book.
Lecturer Class
The Lecturer class inherits from Person and adds attributes and methods specific to lecturers.

Attributes:
office_number (str): The office number of the lecturer.
modules (list): A list of modules the lecturer is teaching.
post_grad (list): A list of postgraduate students the lecturer is supervising.
borrowed_books (list): A list of books the lecturer has borrowed.
Methods:
__init__(self, name, age, contacts, office_number): Initializes the Lecturer with the given attributes.
add_module(self, module): Adds a module to the lecturer's list of modules.
remove_module(self, module): Removes a module from the lecturer's list of modules.
add_post_grad(self, grad): Adds a postgraduate student to the lecturer's list of supervisees.
borrow_book(self, book_title, due_date): Borrows a book for the lecturer until the specified due date.
return_book(self, book_title): Returns a borrowed book.
get_info(self): Returns a dictionary containing the lecturer's information.
