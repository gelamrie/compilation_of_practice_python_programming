#Ask the user to enter two numbers to be stored in num_1 and num_2
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

if num_1 < num_2: #Compare the numbers to see which one is smaller
    print("The smaller number is", num_1, end= ".") #Print num_1 if it's smaller than num_2
else: 
    print("The smaller number is", num_2, end= ".") #Print num_2 if it's smaller than num_1