#Initialized an empty list
numbers = []
while True: #while loop
    try: 
        numbers.append(int(input("Enter a number: "))) #Add the numbers from the user input to the list
    except ValueError: 
        break #Break if invalid input was entered

#Compute for the average
if numbers: 
    average = sum(numbers) / len (numbers) #Create formula
    print("The average is", average, end= ".") #Print the average
else: 
    print("No numbers entered.")#Print "No numbers entered" if there's no number detected