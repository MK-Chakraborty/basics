phonebook = dict()
contacts = ""


def save_contact():
    phonebook[input("Contact name: ")] = input("Enter contact no: ")
    print("contact saved successfully")


def search_contact():
    c = phonebook.get(input("Enter name for search: "))
    print(c)


def delete_contact():
    del phonebook[input("Enter name to delete contact: ")]


def full_phonebook():
    for name, contact_no in phonebook.items():
        print(name, contact_no, "\n")


while contacts.lower() != "s":
    print("What do you want to perform: \nPress 1: To Save a contact no\nPress 2: To search a contact no\nPress 3: To delete a contact\nPress 4: To see phonebook")
    to_do = input("Enter your choice: \n\n")
    if int(to_do) == 1:
        save_contact()
    elif int(to_do) == 2:
        search_contact()
    elif int(to_do) == 3:
        delete_contact()
    else:
        full_phonebook()

    contacts = input(
        "To close the app input s \nOr to do another task input n")
