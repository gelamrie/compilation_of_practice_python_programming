#Create an empty list
numbers = []
while True: #While loop
    try: 
        numbers.append(int(input("Enter a number: "))) #Add the user input to the list
    except ValueError:
        break #Stop when an invalid input is entered

#Display result
if numbers: 
    print("The lowest number is", min(numbers), end= ".") #Print the lowest number if there is any
else: 
    print("No numbers entered") #Print "No numbers entered" if no numbers were entered
