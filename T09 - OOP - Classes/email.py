### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

class Email():

    has_been_read=False


    def __init__(self,email_address,subject_line,email_content):
        self.email_address=email_address
        self.subject_line=subject_line
        self.email_content=email_content
    
    def mark_as_read(self):
        self.has_been_read=True
        print(f"\nEmail {self.email_address} has been marked as 'read'")



# --- Lists --- #
# Initialise an empty list to store the email objects.
    inbox=[]


# --- Functions --- #
# Build out the required functions for your program.

#Creating a dunction to turn the email to be read
# def mark_as_read():
#     has_been_read=True
#     print(f"\nEmail has been marked as 'read'")

    def populate_inbox(self):
        email1=Email("abc@yahoo.com","Email 1","This is content 1")
        email2=Email("def@yahoo.com","Email 2","This is content 2")
        email3=Email("ghk@yahoo.com","Email 3","This is content 3")
        
        # Create 3 sample emails and add it to the Inbox list. 
        self.inbox=[email1,email2,email3]

    def list_emails(self):
        
        # Create a function which prints the email’s subject_line, along with a corresponding number.
        for count in enumerate(self.inbox):
            print(count)

    def read_email(self,index):

        # Create a function which displays a selected email. 
        # Once displayed, call the class method to set its 'has_been_read' variable to True.
        print(self.inbox[index])
        print(self.inbox[index])
        print(self.inbox[index])

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
a=Email.populate_inbox()

print(a)

# Fill in the logic for the various menu operations.
# menu = True

# while True:
#     user_choice = int(input('''\nWould you like to:
#     1. Read an email
#     2. View unread emails
#     3. Quit application

#     Enter selection: '''))
       
#     if user_choice == 1:
#         index=int(input("\nWhich email would you like to read? (0,1,2)"))
#         Email.read_email(index)
        
#     elif user_choice == 2:
#         # add logic here to view unread emails
#         Email.list_emails()
            
#     elif user_choice == 3:
#         # add logic here to quit appplication
#         break

#     else:
#         print("Oops - incorrect input.")

