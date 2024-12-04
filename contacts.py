from validation import validate_phone_number, validate_string

def add_contact(contacts):
    print("\n--- Add a New Contact ---")
    name = input("Enter Name: ")
    if not validate_string(name):
        print("Invalid name. Must be a string.")
        return

    phone = input("Enter Phone Number: ")
    if not validate_phone_number(phone) or phone in contacts:
        print("Invalid or duplicate phone number.")
        return

    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[phone] = {"Name": name, "Email": email, "Address": address}
    print(f"Contact for {name} added successfully.")

def view_contacts(contacts):
    print("\n--- All Contacts ---")
    if not contacts:
        print("No contacts found.")
        return
    for phone, details in contacts.items():
        print(f"Phone: {phone}, Name: {details['Name']}, Email: {details['Email']}, Address: {details['Address']}")

def remove_contact(contacts):
    print("\n--- Remove a Contact ---")
    phone = input("Enter the Phone Number to remove: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact removed successfully.")
    else:
        print("No contact found with that phone number.")

def search_contact(contacts):
    print("\n--- Search Contact ---")
    query = input("Enter name, phone, or email to search: ").lower()
    results = [f"Phone: {phone}, Name: {details['Name']}, Email: {details['Email']}, Address: {details['Address']}"
               for phone, details in contacts.items() if query in phone or query in details['Name'].lower() or query in details['Email'].lower()]
    if results:
        print("\n".join(results))
    else:
        print("No contacts found.")
