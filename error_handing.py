# When we donn't want our program to stop bcz of an error, we use "Try Except Code"i.e error Handling.
a=input("Enter a number:")
print(f" Multiplication table of{a} is:")
try:
    for i in range(1,6):
        print(f"{int(a)}X{i}={int(a)*i}")  # error par is skipped here, and runs further.
except Exception as e:
    print(e)
print("code is further executing.")


