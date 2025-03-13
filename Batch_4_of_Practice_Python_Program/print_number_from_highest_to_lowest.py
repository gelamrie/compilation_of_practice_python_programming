#Create an empty list
numbers = []
while True: #while loop
    try: 
        numbers.append(int(input("Enter a number: ")))#Add the numbers from user input to the list
    except ValueError:
        break #Break if invalid input was entered

#Identify the numbers from highest to lowest
if numbers: 
    numbers.sort(reverse=True) #Use revserse=True to modify the arrangement in descending order 
    print("Numbers from highest to lowest:", numbers, end= ".") #Print numbers from highest to lowest
else:
    print("No numbers entered.")