class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {idx}:")
                print(contact)
                print("--------------------")
        else:
            print("No contacts found.")

    def search_contacts(self, keyword):
        found = False
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                print(contact)
                found = True
        if not found:
            print(f"No contacts found with '{keyword}'.")

    def update_contact(self, keyword):
        found = False
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                print(f"Updating contact: {contact.name}")
                new_name = input("Enter new name (press enter to keep current): ").strip()
                new_phone_number = input("Enter new phone number (press enter to keep current): ").strip()
                new_email = input("Enter new email (press enter to keep current): ").strip()
                new_address = input("Enter new address (press enter to keep current): ").strip()

                if new_name:
                    contact.name = new_name
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                
                print("Contact updated successfully.")
                found = True
                break
        if not found:
            print(f"No contacts found with '{keyword}'.")

    def delete_contact(self, keyword):
        found = False
        for i, contact in enumerate(self.contacts):
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                print(f"Deleting contact: {contact.name}")
                del self.contacts[i]
                print("Contact deleted successfully.")
                found = True
                break
        if not found:
            print(f"No contacts found with '{keyword}'.")

    def load_contacts(self):
        # Example method to load contacts from a file/database
        # This can be extended to load from a CSV, JSON, SQLite, etc.
        # For demonstration, we manually add some contacts here
        self.contacts.append(Contact("John Doe", "1234567890", "john.doe@example.com", "123 Main St"))
        self.contacts.append(Contact("Jane Smith", "9876543210", "jane.smith@example.com", "456 Elm St"))

    def save_contacts(self):
        # Example method to save contacts to a file/database
        # This can be extended to save to a CSV, JSON, SQLite, etc.
        # For demonstration, we print contacts to console
        for contact in self.contacts:
            print(contact)
            print("--------------------")

    def display_menu(self):
        print("\n===== Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save Contacts")
        print("7. Exit")

    def run(self):
        self.load_contacts()
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ").strip()

            if choice == '1':
                name = input("Enter name: ").strip()
                phone_number = input("Enter phone number: ").strip()
                email = input("Enter email: ").strip()
                address = input("Enter address: ").strip()
                new_contact = Contact(name, phone_number, email, address)
                self.add_contact(new_contact)
                print(f"Contact '{name}' added successfully.")

            elif choice == '2':
                print("\n===== Contacts List =====")
                self.view_contacts()

            elif choice == '3':
                keyword = input("Enter name or phone number to search: ").strip()
                print("\n===== Search Results =====")
                self.search_contacts(keyword)

            elif choice == '4':
                keyword = input("Enter name or phone number to update: ").strip()
                self.update_contact(keyword)

            elif choice == '5':
                keyword = input("Enter name or phone number to delete: ").strip()
                self.delete_contact(keyword)

            elif choice == '6':
                print("\n===== Saving Contacts =====")
                self.save_contacts()

            elif choice == '7':
                print("Exiting Contact Book. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 7.")


def main():
    contact_book = ContactBook()
    contact_book.run()

if __name__ == "__main__":
    main()
