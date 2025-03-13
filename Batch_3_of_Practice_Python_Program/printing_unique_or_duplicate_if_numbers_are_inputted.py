#Create an empty list 
numbers = []
while True: #Create a while loop 
    try:
        num = int(input("Enter a number: ")) #Get user input
    
        if num in numbers: #Check if the number is already in the list 
            print("Duplicate") #Print "duplicate" if number is in the list
        else: 
            print("Unique") #Print "unique" if number is not in the list
            numbers.append(num) #Add unique numbers to the list
    except ValueError: #Stop when an invalid input is entered 
        break 