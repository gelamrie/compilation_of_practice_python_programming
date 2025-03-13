#Create an empty list
numbers = []
while True: #While loop
    try: 
        numbers.append(int(input("Enter a number: ")))#Add the numbers from user input to the list
    except ValueError:
        break #Break or stop if invalid input entered

#Print the number from lowest to highest
print("Numbers from lowest to highest:", sorted(numbers), end= ".")