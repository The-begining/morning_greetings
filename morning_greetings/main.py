# main.py

import os
import platform
from morning_greetings.conatct_manager import ContactsManager
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message

CONTACTS_FILE = "new_contacts.txt"

def prompt_for_additional_contacts():
    """Ask the user if they want to add more contacts."""
    answer = input("Do you want to add more people to the contact list? (yes/no): ").strip().lower()
    return answer == 'yes'

def open_text_editor():
    """Open the nano editor or notepad to edit the contacts file."""
    # Check the operating system
    if platform.system() == "Windows":
        os.system(f"notepad {CONTACTS_FILE}")
    else:
        os.system(f"nano {CONTACTS_FILE}")

def load_contacts_from_file():
    """Read contacts from the file and return as a list of dictionaries."""
    contacts = []
    if not os.path.exists(CONTACTS_FILE):
        print(f"{CONTACTS_FILE} does not exist. No contacts to load.\n")
        return contacts

    with open(CONTACTS_FILE, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) >= 2:
                name = parts[0].strip()
                email = parts[1].strip()
                preferred_time = parts[2].strip() if len(parts) > 2 else "08:00 AM"
                contacts.append({"name": name, "email": email, "preferred_time": preferred_time})

    return contacts

def send_greetings(contacts_manager):
    """Send greetings to all contacts in the contact list."""
    contacts = contacts_manager.get_contacts()

    if not contacts:
        print("No contacts available to send greetings.")
        return

    for contact in contacts:
        # Generate a personalized message
        message = generate_message(contact['name'])

        # sending the message
        try:
            send_message(contact['email'], message)
            # Log the sent message
            log_message(contact, message)
            print(f"Message sent to {contact['name']}.\n")
        except Exception as e:
            print(f"Failed to send message to {contact['name']}: {str(e)}")

def main():
    contacts_manager = ContactsManager()

    # Always try to load contacts from the file
    new_contacts = load_contacts_from_file()
    if new_contacts:
        contacts_manager.add_multiple_contacts(new_contacts)
        print(f"{len(new_contacts)} contacts loaded from {CONTACTS_FILE}.\n")
        print("Current contacts:")
        contacts_manager.list_contacts()  # Display the list of contacts

    # Check if the user wants to add more people
    if prompt_for_additional_contacts():
        # Open the text editor for the user to add contacts
        print(f"\nPlease add contacts to the {CONTACTS_FILE} file in the following format:")
        print("Name, Email, Preferred Time (optional)")
        print("Example: Alice, alice@example.com, 08:00 AM\n")
        
        open_text_editor()

        #Load the contacts from the file again and add to ContactsManager
        new_contacts = load_contacts_from_file()
        if new_contacts:
            contacts_manager.add_multiple_contacts(new_contacts)
            print(f"{len(new_contacts)} new contacts loaded from {CONTACTS_FILE}.\n")

    #Send greetings to all contacts
    send_greetings(contacts_manager)

if __name__ == "__main__":
    main()
