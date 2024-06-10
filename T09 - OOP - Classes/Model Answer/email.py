"""Auto-graded Task model answers"""

class Email:
    """Class for representing an email"""

    def __init__(self, email_address, subject_line, email_content):
        """Constructor method for the Email class"""
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False


    def mark_as_read(self):
        """
        Method to Mark an email as read
        """
        self.has_been_read = True


    # Class variable used to store and access the emails
    inbox = []


def populate_inbox():
    """
    Populates the inbox with emails
    """
    emails = [Email("person1@hyperiondev.com", "Welcome to HyperionDev!", "This is your welcome email."),
              Email("person2@hyperiondev.com", "Great work on the bootcamp!", "You're making great progress!"),
              Email("person3@hyperiondev.com", "Your excellent marks!", "You're doing amazing, keep it up!")]
    Email.inbox.extend(emails)


def list_emails():
    """
    Displays all the email subject lines with their corresponding email number
    """
    print("\nInbox:")
    for index, email in enumerate(Email.inbox):
        print(f"{index}. {email.subject_line}")


def read_email(index):
    """
    Displays the details of the selected email

    Argument: the selected email number
    """
    # Checks if the selected email number corresponds to an email in the inbox
    if 0 <= index < len(Email.inbox):
        email = Email.inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")

        # Mark the email as read if it hasn't already been read
        if not email.has_been_read:
            email.mark_as_read()
            print(f"\nEmail from {email.email_address} marked as read.\n")

    else:
        print("Invalid email number.")


def view_unread_emails():
    """
    Displays all the unread email subject lines with their corresponding email number
    """
    print("\nUnread Emails:")
    for index, email in enumerate(Email.inbox):
        if not email.has_been_read:
            print(f"{index}. {email.subject_line}")


populate_inbox()

# Main Program
while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

Enter selection: '''))

    if user_choice == 1:
        list_emails()
        index = int(input("Enter the number of the email you want to read: "))
        read_email(index)
    elif user_choice == 2:
        view_unread_emails()
    elif user_choice == 3:
        print("Quitting application.")
        break
    else:
        print("Invalid choice. Please select again.")
