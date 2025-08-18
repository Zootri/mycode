# Contact Management System
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        print(f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}")


class Manager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                contact.display()

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.display()
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted.")
                return
        print("Contact not found.")


manager = Manager()  # Create an instance of Manager

while True:
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        new_contact = Contact(name, phone, email)
        manager.add_contact(new_contact)
        print("Contact added successfully.")

    elif choice == "2":
        manager.view_contacts()

    elif choice == "3":
        search_name = input("Enter name to search: ")
        manager.search_contact(search_name)

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        manager.delete_contact(delete_name)

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
