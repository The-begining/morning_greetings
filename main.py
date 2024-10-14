from morning_greetings.conatct_manager import ContactsManager
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message
from morning_greetings.logger import log_message

def main():
    contact_manager = ContactsManager()

    # Example: Add some contacts
    contact_manager.add_contact("Alice", "alice@example.com", "08:00 AM")
    contact_manager.add_contact("Bob", "bob@example.com", "09:00 AM")
    contact_manager.add_contact("Charlie", "charlie@example.com", "07:30 AM")

    # Get all contacts
    contacts = contact_manager.get_contacts()

    for contact in contacts:
        # Generate a personalized message
        message = generate_message(contact['name'])

        # Simulate sending the message
        try:
            send_message(contact['email'], message)
            # Log the sent message
            log_message(contact, message)
        except Exception as e:
            print(f"Failed to send message to {contact['name']}: {str(e)}")

if __name__ == "__main__":
    main()
