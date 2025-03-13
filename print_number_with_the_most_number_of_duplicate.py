#Create an empty list
numbers = []
while True: #While loop
    try: 
        numbers.append(int(input("Enter a number: ")))#Add user input to the list
    except ValueError:
        break #Break or stop if an invalid input was entered
#Identify the number that has the most duplicate
    #Print the number with most duplicates
    #If there's no number entered, print "No numbers entered."