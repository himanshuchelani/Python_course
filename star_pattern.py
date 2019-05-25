1
12
123
1234
12345
n=int(input("enter the number of rows"))                
for i in range(1,n+1):
    for j in range(1,i+1):                                
        print(j,end="")
    print()






1
22
333
4444
55555
n=int(input("enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
    





1
22
333
4444
55555        
n=int(input("enter the rows"))
for row in range(n):
    for col in range(n):
        if col==0 or row==n-1 or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()
    
    
    
    

    
    
    
    
    
    

    
