
number = input("enter space separated input")
x = number.split(" ")
print(x)

for i in x:
    
    if(int(i)>0 and i[ ::-1]==i):
        print("True")
    else:
        print("false")