#Initialize an empty list to store numbers
numbers = []

#Ask the user to input 10 numbers
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

#Compute the result by subtracting the sum of remaining numbers
result = numbers[0] - sum(numbers[1:]) 

#Print the result
