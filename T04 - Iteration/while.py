#Practical Task 1

user_input=0
count=0
number=0

while user_input!=-1:
    user_input=int(input("Please enter a number from 0 to 10: "))
    number+=user_input
    count+=1
    print(number)   #print to see how the number changes within the loop
    print(count)    #print to see how the count changes within the loop

#When the while condition is false, we will exit the while loop

average=(number+1)/(count-1)         #adding 1 to number to compensate the -1 to exit the loop,   subtracting 1 to count to discount the last loop 
print(f" The average of the number types in is: {average}")