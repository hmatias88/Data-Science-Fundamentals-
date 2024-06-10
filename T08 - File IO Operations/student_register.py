#This is the Practical Task 2

#This program allows the user to register students for an exam venue

#Asks for user input
no_students=int(input("How many students are registering for the exam?:\n"))

#Making use of the with method to open the file in w+ mode.
with open('reg_form.txt','w+') as f:

    #Looping through the number of students specified by the user
    for i in range(0,no_students):
        #asks for user input for the student ID
        student_id=input("What is the student ID number?: ")
        #Writes the student id to the text file.
        f.write(student_id + " .............................. "+"\n")

#Final printing to let the user know how many students have been registered.
print(f"\nStudents record sucessfully registered. A total of {no_students} have been registered for the exam!\n")