number=int(input("enter the number:"))
result=0
n=len(str(number))
while(number!=0):
    digit=number%10
    result=result+digit**n
    number=number//10
if(result == number):
    print("Armstrong number")

    
    
    

for i  in range(1001):
    number=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if result==number:
        print(number)
      