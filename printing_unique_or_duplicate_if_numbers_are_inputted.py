#Create an empty list 
numbers = []
while True: #Create while loop 
    try:
        num = int(input("Enter a number: "))#Get user input
    
    if num in numbers: #Check if the number is already in the list 
        print("Duplicate") #Print "duplicate" if number is in the list
    else: 
        print("Unique") #Print "unique" if number is not in the list

#Stop when an invalid input is entered 