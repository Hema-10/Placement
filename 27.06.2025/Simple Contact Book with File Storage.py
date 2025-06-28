def add_contact(name, phone):
    with open("contacts.txt", "a") as f:
        f.write(f"{name},{phone}\n")

def view_contacts():
    with open("contacts.txt", "r") as f:
        for line in f:
            name, phone = line.strip().split(",")
            print(f"Name: {name}, Phone: {phone}")

add_contact("Alice", "9876543210")
view_contacts()
