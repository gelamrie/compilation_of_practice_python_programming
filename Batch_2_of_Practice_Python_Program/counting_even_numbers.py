#Initialize a counter for even numbers to 0
even_num = 0 
for i in range(10): #Loop 10 times to get user input
    if int(input("Enter a number: ")) % 2 == 0: #Check if the number is even
        even_num += 1 #If even, increment the counter

print("The number of even numbers is", even_num) #Print the count of even numbers
