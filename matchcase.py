# OUICK NOTE

# This imports the os module, which provides a way to use operating system dependent functionality like reading 
import os
os.system("python --version")

''' 
* print("Current directory:", os.getcwd())  # Prints current working directory

* os.mkdir("new_folder")  # Creates a new folder named 'new_folder'

* os.chdir("new_folder")  # Changes the current working directory to '''

# Matchcase Statements
''' We may switch case-like characteristics very similar to if-else functionality. We 
use a match case in Python. If you are coming from a C, English, or Java-language, you
must have heard of switch-case statements. A match statement will compare or give the
variable's value in different shapes or selected to as the pattern. The main idea is
to take or compare the variable with all the present patterns and to make this into one.

The matchcase consists of three main entities:
1. match keyword: This is the keyword that starts the match case statement.
2. one or more case clause: These are the clauses that contain the patterns to be matched and executed.
3. default clause(expression for each case): This is the clause that is executed if none of the patterns match.'''
 # example:

x=int(input(" Enter a number"))
# x is a variable to match.
match x:
    case 0:        # This is the first case clause
        print("You entered zero") # executed only if x=0
    case 1:
        print("You entered one")
    case 4:
        print("You entered four")
    case _:
        print("You entered something else")  # This is the default clause, executed if none of the above cases match.


              








