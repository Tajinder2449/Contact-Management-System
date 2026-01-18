contacts = {}

while True:
    print("\n1. Add new number")
    print("2. Search contact number")
    print("3. Update number")
    print("4. Remove number")
    print("5. Show all the numbers")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter the name: ").lower()
        number = input("Enter the contact number: ")
        contacts[name] = number
        print("Contact Added")

    elif choice == 2:
        name = input("Enter name to search: ").lower()
        if name in contacts:
            print(f"{name.capitalize()} : {contacts[name]}")
        else:
            print("Contact not found")

    elif choice == 3:
        name = input("Enter name to update contact number: ").lower()
        if name in contacts:
            contacts[name] = input("Enter the new number: ")
            print("Contact Updated")
        else:
            print("Contact not found")

    elif choice == 4:
        name = input("Enter name to delete contact number: ").lower()
        if name in contacts:
            del contacts[name]
            print("Contact Removed")
        else:
            print("Contact not found")

    elif choice == 5:
        if not contacts:
            print("No contacts available")
        else:
            print("\nContact List:")
            for name, number in contacts.items():
                print(f"{name.capitalize()} : {number}")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Enter a valid choice")
