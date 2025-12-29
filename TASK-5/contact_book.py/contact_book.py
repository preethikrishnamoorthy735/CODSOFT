# Contact Book Application - Task 5

contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
        print(f"Address: {details['address']}")
        print("-" * 20)

def search_contact():
    search = input("Enter name or phone number to search: ").strip()

    for name, details in contacts.items():
        if search == name or search == details["phone"]:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            return

    print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("Enter new details (leave blank to keep old value)")

    phone = input("New phone number: ")
    email = input("New email: ")
    address = input("New address: ")

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    if address:
        contacts[name]["address"] = address

    print("Contact updated successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def show_menu():
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")