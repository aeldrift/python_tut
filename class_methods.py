# Example: Instance method:

class MyClass:
    class_var = 0

    def __init__(self, value):
        self.instance_var = value  # unique for each object

    def show_data(self):
        print(f"Instance variable: {self.instance_var}")
        print(f"Class variable: {MyClass.class_var}")
# Now, differentiating Class & Instance methods. Example:

class BankAccount:
    bank_name = "XYZ Bank"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")

# Creating instances
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

acc1.deposit(200)  # Works only for Alice
acc2.deposit(100)  # Works only for Bob

# Practice Question:
''' Create a class Library where:
1. Each book has a title and author → that belongs to an instance.
2. The library has a shared rule: the late fee per day (same for all books).
3. Write: An instance method show_book() that prints the book’s title and author.
A class method change_late_fee() that changes the late fee for all books.'''