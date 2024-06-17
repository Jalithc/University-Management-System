from datetime import date

class Person:
    '''Initialize the person's name, age, and contacts in the super class and create a class that inherits from the Person class.
    Create a list to add modules that students are enrolled in.'''
    def __init__(self, name, age, contacts):
        self.name = name
        self.age = age
        self.contacts = contacts

class Student(Person):
    def __init__(self, name, age, contacts, student_ID, year_of_entry):
        super().__init__(name, age, contacts)
        self.student_ID = student_ID
        self.year_of_entry = year_of_entry
        self.enroll_modules = []
        # To keep track of borrowed books
        self.borrowed_books = []
    
    def enroll_module(self, module):
        self.enroll_modules.append(module)
        print(f"Module '{module}' has been added to {self.name}'s enrolled modules.")

    def borrow_book(self, book_title, due_date):
        book = {'title': book_title, 'due_date': due_date}
        self.borrowed_books.append(book)
        print(f"Book '{book_title}' borrowed until {due_date}.")
    
    def return_book(self, book_title):
        for book in self.borrowed_books:
            if book['title'] == book_title:
                self.borrowed_books.remove(book)
                print(f"Book '{book_title}' returned!")
                return
        print(f"Book '{book_title}' not found among borrowed books!")

class Lecturer(Person):
    def __init__(self, name, age, contacts, office_number):
        super().__init__(name, age, contacts)
        self.office_number = office_number
        self.modules = []
        self.post_grad = []
        # To keep track of borrowed books
        self.borrowed_books = []

    def add_module(self, module):
        if module not in self.modules:
            self.modules.append(module)
            print(f"Module '{module}' has been added to the list of modules.")
        else:
            print(f"Module '{module}' is already in the list of modules!")

    def remove_module(self, module):
        if module in self.modules:
            self.modules.remove(module)
            print(f"Module '{module}' has been removed from the list of modules.")
        else:
            print(f"Module '{module}' is not in the list of modules!")

    def add_post_grad(self, grad):
        if grad not in self.post_grad:
            self.post_grad.append(grad)
            print(f"Postgraduate student '{grad}' has been added to the list of supervisees.")
        else:
            print(f"Postgraduate student '{grad}' is already in the list of supervisees!")

    def borrow_book(self, book_title, due_date):
        book = {'title': book_title, 'due_date': due_date}
        self.borrowed_books.append(book)
        print(f"Book '{book_title}' borrowed until {due_date}.")

    def return_book(self, book_title):
        for book in self.borrowed_books:
            if book['title'] == book_title:
                self.borrowed_books.remove(book)
                print(f"Book '{book_title}' returned!")
                return
        print(f"Book '{book_title}' not found among borrowed books!")

    def get_info(self):
        return {
            'name': self.name,
            'age': self.age,
            'contacts': self.contacts,
            'office_number': self.office_number,
            'modules': self.modules,
            'postgraduate_students': self.post_grad,
            'borrowed_books': self.borrowed_books
        }

# Example
lecturer = Lecturer('Dr. John Doe', 45, '070101010', 'Room 123')
lecturer.add_module('Artificial Intelligence')
lecturer.add_post_grad('Alice Johnson')

# Borrowing and returning books
lecturer.borrow_book('Introduction to Machine Learning', date(2024, 7, 1))
lecturer.borrow_book('Advanced Data Science', date(2024, 8, 15))
lecturer.return_book('Introduction to Machine Learning')


