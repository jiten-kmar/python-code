#Python Program to Put Even and Odd elements in a List into Two Different Lists
#The program takes a list and puts the even and odd elements in it into two separate lists.
list1=[]
list2=[]
total_number=int(input("Enter how many numbers you want to put in list: "))
for n in range(0, total_number):
    number=int(input("Enter the number for the list: "))
    if number%2==0:
        print("Number entered is even")
        list1.append(number)
    else:
        print ("number entered is odd")
        list2.append(number)
print ("Even list is: ", list1)
print ("Odd list is ", list2)
