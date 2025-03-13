#Create an empty list
numbers = []
while True: #While loop
    try: 
        numbers.append(int(input("Enter a number: "))) #Add user input to the list
    except ValueError:
        break #Break or stop if an invalid input was entered
if numbers: 
    most_common = max(set(numbers), key=numbers.count) #Identify the number that has the most duplicate
    print("The number with most duplicates is", most_common, end= ".") #Print the number with most duplicates
else: 
    print("No numbers entered.") #If there's no number entered, print "No numbers entered.