# Example: Instance method:

class MyClass:
    class_var = 0

    def __init__(self, value):
        self.instance_var = value  # unique for each object

    def show_data(self):
        print(f"Instance variable: {self.instance_var}")
        print(f"Class variable: {MyClass.class_var}")