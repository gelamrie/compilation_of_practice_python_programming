#Initialize a counter for odd numbers to 0
odd_num = 0
for i in range(10): #Loop 10 times to get user input
    if int(input(f"Enter a number: ")) % 2 != 0: #Check if the number is odd
        odd_num += 1 #If odd, increment the counter
print("The number of odd numbers is", odd_num, end= ".") #Print the count of odd numbers