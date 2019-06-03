list1=[22,32,11,45,76,55]
for j  in range(len(list1)-1):
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
            print(list1)
        else:
            print(list1)
    print()
print("sorted list",list1)
    
