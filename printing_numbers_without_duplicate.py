#Ask user to input 10 numbers and store them in a list
numbers = [int(input("Enter a number: ")) for i in range (10)]

#Identify numbers that appear only once in the list 
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

#Print the unique numbers
print("The numbers without duplicates is/are", unique_numbers, end= ".")