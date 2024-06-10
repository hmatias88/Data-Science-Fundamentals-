#Practical Task 2

#The aim of this code is to produce the below pattern

import math

"""

*
**
***
****
*****
****
***
**
*

9 rows

"""

n=int(input("Please define the number of rows: "))       #number of rows, up to the user to define, we can use 9 for the time being

if n%2==0:
    print("Even rows")
else:
    print("Odd rows")    

count=0                         #Initializing count outside of the for loop       

for i in range(1,n+1):          #adding 1 to n, as we are starting from i=1
    if i<math.ceil(n/2):        #adding the * in ascending order up to just before the middle row
        result="*"*i
        print(result)
    else:  
        result="*"*(i+count)
        print(result)
        count-=2                #counter to reduce 2no of * each time a loop is completed


