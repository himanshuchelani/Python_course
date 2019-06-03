from math import factorial as fact
number=int(input("enter the number"))
fact(number)



def factorial(n):
    if n==0:
        return 1
    else:
        return  n*factorial(n-1)
n=int(input("enter the number:"))
print(factorial(n))
