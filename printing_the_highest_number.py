#Create an empty list
numbers = [] 
while True: #while loop
    try: 
        numbers.append(int(input("Enter a number: "))) #Add user input to the list
    except ValueError: 
        break #Break if invalid input was entered

#Identify the highest number
if numbers: 
    print("The highest number is", max(numbers), end= ".") #Print the highest number
else: 
    print("No numbers entered.")#Else, print "No numbers entered." if there are no numbers detected