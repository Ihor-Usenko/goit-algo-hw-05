def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error_add(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner


@input_error_add
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def input_error_change(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me name and phone please."

    return inner


@input_error_change
def change_phone(args, contacts):
    if args[0] in contacts:
        contacts[args[0]] = args[1]
        return f"New phone '{args[1]}' for contact '{args[0]}' is saved."
    else:
        return f"Contact '{args[0]}' is not found!"


def input_error_phone(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "You have't entered a contact name!"
        except KeyError:
            return "Contact is not found!"

    return inner


@input_error_phone
def show_phone(args, contacts):
    if args[0] in contacts:
        return contacts[args[0]]
    else:
        raise KeyError


def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(f"How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
