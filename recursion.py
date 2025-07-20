# write a program to calcute factorial of given no.
def fac(n):
    if (n==0 or n==1):
        return 1
    else:
        return n* fac(n-1)
print("factorial of 0 is",fac(6))
print("factorial of 0 is", fac(0))

# write a program to calculate valu of given no. in fibanocci series.
def fib(n):
    if (n==0 or n==1):
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(3))
print(fib(0))
print(fib(4))
print(fib(5))

# Recursion: A function that calls itself repeatedly until a base condition is met.
# WAP to print numbers from 5 to 1 using recursioin.
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
show(5)