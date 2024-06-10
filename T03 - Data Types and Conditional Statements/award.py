# Auto-graded task 3


#Asking user to input the time taken to complete different activities
swimming=int(input("How many minutes did it take to complete swimming? "))
cycling=int(input("How many minutes did it take to complete cycling? "))
running=int(input("How many minutes did it take to complete running? "))

total_time=swimming+cycling+running
print(f'The total time taken to complete the triathlon is {total_time} minutes')

if total_time<=100:
    print("Provincial colours")
elif total_time>100 and total_time<=105:
    print("Provincial half colours")
elif total_time>106 and total_time<=110:
    print("Provincial scroll")
else:
    print("No Award")