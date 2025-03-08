#Ask the user to enter two numbers to be stored in num_1 and num_2
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if num_1 > num_2: #Compare the numbers to see which one is bigger 
    print("The bigger number is", num_1) #print num_1 if it's bigger than num_2
else: 
    print("The bigger number is", num_2) #print num_2 if it's bigger than num_1