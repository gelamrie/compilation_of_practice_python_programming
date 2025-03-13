#Create an empty list to store numbers
numbers = []
for i in range (10): #Create a loop to get the user input
    num = int(input("Enter a number: "))
    if num not in numbers: #Add number only if it is not in the list already
        numbers.append(num)

#Print the list 
print("Here are the numbers with first occurrences only:", numbers, end= ".")