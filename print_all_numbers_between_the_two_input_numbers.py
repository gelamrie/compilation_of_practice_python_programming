#Get input from the user
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

#Ensure 'num_1' is the smaller number
if num_1 > num_2:
    num_1, num_2 = num_2, num_2 
    
#Print numbers between 'num_1' and 'num_2'