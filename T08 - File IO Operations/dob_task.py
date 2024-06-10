#This is the Practical Task 1


#Reading the DOB.txt file

with open('Input Code Files\Task file\DOB.txt', 'r') as file:
    lines=file.readlines()

    print("\nName:")
#Looping through each line. Splitting each line where we have the white space into a list for each line.
#Then printing the first 2 items in the list which corresponds to first & last name.
    for line in lines:
        s_line=line.split()
        print(f"{s_line[0]} {s_line[1]}")

    print("\nBirth Date:")
#Basically doing the same as above, but printing the last 3 items of the list which corresponds to DOB
    for line in lines:
        s_line=line.split()
        print(f"{s_line[2]} {s_line[3]} {s_line[4]}")
        