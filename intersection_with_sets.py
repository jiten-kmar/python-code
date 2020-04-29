#Python Program to Find the Intersection of Two Lists with sets
def inter(lista,listb):
    return list(set(lista) & set(listb))
list1=[]
list2=[]
total_n_list1=int(input("Enter how many numbers you need in list1: "))
for n1 in range(0,total_n_list1):
    num1=int(input("Enter the number for list1: "))
    list1.append(num1)
print(list1)
total_n_list2=int(input("Enter how many numbers you need in list2: "))
for n2 in range(0,total_n_list2):
    num2 = int(input("Enter the number for list2: "))
    list2.append(num2)
print(list1)
#list1 & list2
print(inter(list1,list2))

