# This is how I will solve the task:

#1  Using the input() function to get the following information from the user: Name, Age, House_Number, Street_Name
#2  use the f-string approach to use the print() function to print out the following sentence:
#3  "This is {Name}. He is {Age} years old and lives at {House Number} {Street_Name}"
#4

#================================================


#Task 3 Code:

Name=str(input("What is your name?: "))
Age=int(input("What is your age?: "))
House_Number=int(input("What is your house number?: "))
Street_Name=str(input("What is your street name?: "))

print((f"This is {Name}. He is {Age} years old and lives at {House_Number} {Street_Name}"))