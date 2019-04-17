character=0

lines=0
b=0
with open("words.txt",'rt') as rd:
    for line in rd.readlines():
           lines+=1 
           a=line.split()
           print(a)
           b+=len(a)
           print("words:",b)
           for i in line:
               if(i.isalnum() or i.isspace()):
                   character+=1
print("line:",lines)
print("character:",character)


    
