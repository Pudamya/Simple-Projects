def add_contact(contacts):
    """
    Add a new contact.
    """
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added successfully.")

def view_contact_list(contacts):
    """
    Display list of all contacts.
    """
    if contacts:
        print("Contact List:")
        for name, contact_info in contacts.items():
            print(f"Name: {name}, Phone: {contact_info['phone']}")
    else:
        print("Contact list is empty.")

def search_contact(contacts):
    """
    Search for a contact by name or phone number.
    """
    keyword = input("Enter name or phone number to search: ")
    found = False
    for name, contact_info in contacts.items():
        if keyword in (name, contact_info['phone']):
            print(f"Name: {name}, Phone: {contact_info['phone']}, Email: {contact_info['email']}, Address: {contact_info['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact(contacts):
    """
    Update contact details.
    """
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Current Details:")
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}, Address: {contacts[name]['address']}")
        choice = input("Enter the field to update (phone/email/address): ")
        if choice in ('phone', 'email', 'address'):
            new_value = input(f"Enter new {choice}: ")
            contacts[name][choice] = new_value
            print("Contact updated successfully.")
        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """
    Delete a contact.
    """
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def main():
    """
    Main function to interact with the user.
    """
    contacts = {}
    while True:
        print("\n1. Add Contact\n2. View Contact List\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contact_list(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
