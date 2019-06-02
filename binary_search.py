def binary_search(list1,key):
    low=0
    high=len(list1)-1
    Found=False
    while low<=high and not Found:
        mid=(low+high)//2
        if key==list1[mid]:
            Found=True
        elif key>list1[mid]:
            low=mid+1
        else:
            high=mid-1
    if Found ==True:
        print("key is found")
    else:
        print("key not found")

list1=[2,1,8,69,68,98,45,35,54]
list1.sort()
key=int(input("enter the key"))
binary_search(list1,key)
