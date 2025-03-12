#Ask user to enter two numbers that will be stored in num_1 and num_2
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if num_2 != 0: #Check if num_2 is not equal to zero
    quotient = num_1 / num_2 #If true, solve for the quotient 
    print (f"The quotient of the two numbers is {quotient:2f}.") #Display the quotient with decimal places

#If num_2 is equal to zero, diplay "Division by zero is not allowed"
else:
    print("Division by zero is not allowed")