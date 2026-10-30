
print("CONTACT BOOK USING FUNCTIONS")
print("1. ADD CONTACTS")
print("2. SEARCH CONTACTS")
print("3. UPDATE CONTACT")
print("4. DELETE CONTACT")
print("5. VIEW CONTACTS")

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter mobile number: ")
    contacts[name] = phone
    print("Contact", name, "is added")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("Contact found")
        print("Name:", name)
        print("Phone:", contacts[name])
    else:
        print("Contact not found")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        contacts[name] = input("Enter new phone number: ")
        print("Contact is updated")
    else:
        print("Contact not found")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact is deleted")
    else:
        print("Contact not found")

def display_contact():
    if contacts:
        for name, phone in contacts.items():
            print("Name:", name, "| Phone:", phone)
    else:
        print("No contacts available")

while True:
    option = int(input("Enter option : "))

    if option == 1:
        add_contact()
    elif option == 2:
        search_contact()
    elif option == 3:
        update_contact()
    elif option == 4:
        delete_contact()
    elif option == 5:
        display_contact()
    elif option == 6:
        print("Exiting contact book")
        break
    else:
        print("Invalid option")
