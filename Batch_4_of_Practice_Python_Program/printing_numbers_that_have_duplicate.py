#Ask user to input 10 numbers and store them in a list
numbers = [int(input("Enter a number: ")) for i in range (10)]

#Identify numbers that appear mutiple time in the list
duplicates = sorted(set(num for num in numbers if numbers.count(num) > 1))

#Print the numbers that has duplicate
if duplicates:
    print("The number/s that has duplicate is/are", duplicates, end= ".")
else:
    print("No duplicate numbers found.")