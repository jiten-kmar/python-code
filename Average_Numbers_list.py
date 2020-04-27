## Python Program to Calculate the Average of Numbers in a Given List
list1 = []
Sum = 0
total_numbers = int(input("Enter how many numbers needed in the list: "))
for number in range(0, total_numbers):
    number1 = int(input("Enter the number: "))
    list1.append(number1)
Sum = sum(list1)
print(list1)
print(Sum)
avg=sum(list1)/total_numbers
print ("Avg is: ", round(avg,2))

