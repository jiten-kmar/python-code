
list1=[]
ele=int(input("Enter how many elements you need: "))
for i in range(0, ele):
    value=(input("Enter the element : "))
    list1.append(value)
list1.sort(key=len)
print(list1)

