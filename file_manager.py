import csv

FILE_PATH = "contacts.csv"

def load_contacts():
    contacts = {}
    try:
        with open(FILE_PATH, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts[row["Phone"]] = {"Name": row["Name"], "Email": row["Email"], "Address": row["Address"]}
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts):
    with open(FILE_PATH, mode="w", newline="") as file:
        fieldnames = ["Phone", "Name", "Email", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for phone, details in contacts.items():
            row = {"Phone": phone, "Name": details["Name"], "Email": details["Email"], "Address": details["Address"]}
            writer.writerow(row)
    print("Contacts saved successfully.")
