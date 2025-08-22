# Practice Question:

''' OOP + Practical
“Design a Python class to represent a library book system where each book has a title, author, issue date, and due date. The system should also calculate fines for overdue books. '''

import random
from datetime import date, timedelta

class Library:
    late_fee = 10   # fee per day after due date (integer)

    def __init__(self, title, author, random_issue=False):
        self.title = title
        self.author = author

        if random_issue:  # pick a random date in the last 100 days
            days_ago = random.randint(1, 100)
            self.issue_date = date.today() - timedelta(days=days_ago)
        else:
            self.issue_date = date.today()

        self.due_date = self.issue_date + timedelta(days=30)

    def show_book(self):
        print(f"The Book '{self.title}' is written by {self.author}")
        print(f"Issued on: {self.issue_date}")
        

    def calculate_fine(self):
        today = date.today()
        print("Today's date:", today)
        print("Due date:", self.due_date)

        if today > self.due_date:
            overdue_days = (today - self.due_date).days
            fine = overdue_days * Library.late_fee
            print("Overdue days:", overdue_days)
            print("Late fee per day:", Library.late_fee)
            return fine
        else:
            print("No fine, still within due date.")
            return 0

#   @classmethod
#    def update_fee(cls, new_fee):
#       cls.late_fee = new_fee


# Example with random issue date
book1 = Library("ABC", "Alice", random_issue=True)
book1.show_book()
print("Fine:", book1.calculate_fine())

# Update fee
#Library.update_fee(20)
