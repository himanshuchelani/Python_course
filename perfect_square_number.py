n=int(input("enter the no"))
result=0
for i in range(1,n):
    if n%i==0:
        result=result+i
    elif n==result:
        print(n,"perfect square no.")
    else:
        print(n,"not perfect square")