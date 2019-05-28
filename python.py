"""p
py
pyt
pyth
pytho
python
 """   
    
    
    
    
    
n=input("enter the string")
length=len(n)
for row in range(length):
    for col in range(row+1):
        print(n[col],end="")
    print()
        
        