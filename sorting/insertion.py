def insertion(list1):
    for i in range(1,len(list1)):
        current_element=list1[i]
        pos =i
        while current_element<list1[pos-1]&pos>0:
            list1[pos]=list1[pos-1]
            pos=pos-1
        list1[pos]=current_element 
list1=[2,1,6,4,9]
insertion(list1)
print(list1)