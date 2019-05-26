*****
 *  *
  * *
   **
    *

n=int(input("enter the number of rows"))
for row in range(0,n):
    for col in range(0,n):
        if(row==0 or col==(n-1) or row==col):
            print("*",end="")
        else:
            print(end=" ")
    print()








1
23
456
78910  

num=1
n=int(input("enter the  number of rows"))
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end="")
        num=num+1
    print()