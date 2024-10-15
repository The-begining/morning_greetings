# contacts_manager.py

class ContactsManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        """Add a single contact."""
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)

    def add_multiple_contacts(self, contacts_list):
        """Add multiple contacts at once."""
        for contact in contacts_list:
            name = contact.get('name')
            email = contact.get('email')
            preferred_time = contact.get('preferred_time', "08:00 AM")
            self.add_contact(name, email, preferred_time)

    def remove_contact(self, name):
        """Remove a contact by name."""
        self.contacts = [c for c in self.contacts if c['name'] != name]

    def get_contacts(self):
        """Return the list of contacts."""
        return self.contacts

    def list_contacts(self):
        """List all current contacts."""
        if not self.contacts:
            print("No contacts found.\n")
        else:
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
