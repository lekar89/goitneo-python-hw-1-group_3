
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    try:
        contacts[name]
        contacts[name] = phone
        return "Contact updated."
    except:
        return "Contact not found."

def get_contact_phone(args, contacts):
    name = args[0]
    try:
        phone  = contacts[name]
        return phone
    except:
        return "Contact not found."
    
def show_all(contacts):
    if len(contacts) == 0:
        return "No contacts."
    res = ""
    for k,v in contacts.items():
        res = res + f"Contact {k} {v}."
    return res

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact_phone(args, contacts))
        elif command == "all":
            print(show_all( contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
