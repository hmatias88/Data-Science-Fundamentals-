# Practical Task 1

# 1st Example---------------------------------------------------------------------------------------------------------------------

# Asking the user to input a sentence
input_string=input("Please type your words here: \n") # The default is Hello World

#turning the input into all lower case
s_input_string=input_string.lower()


# initializing an empty string where we will be concatenating the modified letters and joining it together to form the modified sentence.
upper_mod_string=""

#Looping through s_input_string and concatenating to the empty string upper_mod_string.
#The code turns the 1st letter and the every other letter (even index) into an upper case

for i in range(0,len(s_input_string)):
    if i==0 or i%2==0:
        upper_mod_string+=s_input_string[i].upper()
    else:
        upper_mod_string+=s_input_string[i]

print(upper_mod_string)

# 2nd example--------------------------------------------------------------------------------------------------------------------

# Input sentence, using the example given to test whether it works. By default we turn the whole sentence to lowercase first.
input_sentence=input("Please type your sentence here: \n").lower()  # "I am learning to code"

#Splitting the input sentence into a list of words that have lowered case
s_input_sentence=input_sentence.split(" ")

#Initializing an empty list
mod_sentence=[]

# Adding the words back to the empty list mod_sentence with different character cases depending on the index of the list.
for i in range(0,len(s_input_sentence)):
    if i==0 or i%2==0:
        mod_sentence.append(s_input_sentence[i])
    else:
        mod_sentence.append(s_input_sentence[i].upper())

# Joining the individual words back together but separated by a space.
print(" ".join(mod_sentence))