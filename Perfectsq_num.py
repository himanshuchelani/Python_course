result=0
num=int(input("enter the number"))
for i in range(1,num):
    if num%i==0:
        result+=i
    elif result==num:
        print(":Perfecr Square number:")
    else:
        print(":Not a Perfect Square number:")()