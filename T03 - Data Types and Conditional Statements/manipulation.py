#This is the autograded task 1

str_manip=input("Please enter a sentence: ")

print(len(str_manip))
print(str_manip[-1:])
last_letter=str_manip[-1:]
print(str_manip.replace(last_letter,"@"))

last_three=str_manip[-3:]
print(last_three)

five_letter_word=str_manip[:3]+str_manip[-2:]
print(five_letter_word)