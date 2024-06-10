class Email():

    has_been_read=False


    def __init__(self,email_address,subject_line,email_content):
        self.email_address=email_address
        self.subject_line=subject_line
        self.email_content=email_content


#Creating an empty inbox list
inbox=[]

#instantiating 3 email class objects
def populate_inbox():
    
    email1=Email("abc@yahoo.com","Email 1","This is content 1")
    email2=Email("def@yahoo.com","Email 2","This is content 2")
    email3=Email("ghk@yahoo.com","Email 3","This is content 3")
    inbox=[email1,email2,email3]

# print(email1.email_address)
# print(email1.email_content)



def list_email():
    for count,i in enumerate(inbox):
        print(count, i.subject_line)

populate_inbox()
list_email()