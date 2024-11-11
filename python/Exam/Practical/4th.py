# Contact Book Application

# Initialize an empty list to store contacts
contacts = []

def add_contact(name, phone):
    """Add a new contact to the contact book."""
    contact = {
        'name': name,
        'phone': phone
    }
    contacts.append(contact)
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    """Display all contacts in the contact book."""
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(name):
    """Search for a contact by name."""
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found Contact - Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
            break
    if not found:
        print(f"No contact found with the name '{name}'.")

def delete_contact(name):
    """Delete a contact by name."""
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    print(f"Contact '{name}' deleted successfully." if len(contacts) < len(contacts) else f"No contact found with the name '{name}'.")

def main():
    """Main function to run the contact book application."""
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to search: ")
            search_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '5':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()