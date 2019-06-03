list1=[22,32,11,45,76,55]
for i in range(len(list1)):
    min_value=min(list1[i:])
    min_index=list1.index(min_value)
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)    