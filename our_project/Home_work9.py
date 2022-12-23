Phonebook = {}

def input_error(func):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, *kwargs)
        except ValueError:
            return f"Phone number has to be a number"
        except IndexError:
            if func.__name__ in ["add", "change"]:
                return f"Give me name and phone please"
            if func.__name__ == "phone":
                return "Please give a name"
        except KeyError as e:
            return f"Not contact {e} in Phone book"
    return wrapper


def hello():
    return "How can I help you?"

def modified_number(phone_number):
    new_phone = (
        phone_number.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


@input_error
def add(user_data):
    if not user_data.split()[2].isnumeric():
        raise ValueError
    Phonebook[user_data.split()[1]] = user_data.split()[2]
    return f"Number {user_data.split()[2]} for {user_data.split()[1]} has been added"

@input_error
def change(user_data):
    if not user_data.split()[2].isnumeric():
        raise ValueError
    if user_data.split()[1] in Phonebook.keys():
        Phonebook[user_data.split()[1]] = user_data.split()[2]
        return f"Number {user_data.split()[2]} for {user_data.split()[1]} has been changed"
    else:
        raise KeyError(user_data.split()[1])


@input_error
def phone(user_data):
    return Phonebook[user_data.split()[1]]

def show_all():
    return Phonebook


def end_work():
    return "Good bye"



COMMANDS = {"hello": hello,
            "add": add,
            "change": change,
            "phone": phone,
            "show": show_all,
            "end_work": end_work}

def parser(command):
    if command.lower() == "hello":
        return "hello"
    if command.lower() in ["good bye", "close", "exit"]:
        return "end_work"
    if command.split()[0].lower() == "add":
        return "add"
    if command.split()[0].lower() == "change":
        return "change"
    if command.split()[0].lower() == "phone":
        return "phone"
    if command.split()[0].lower() == "show":
        return "show"
    else:
        return "wrong_command"


def main():
    while True:
        user_command = input(">>> ")
        command = parser(user_command)
        if command == "end_work":
            print(COMMANDS["end_work"]())
            break
        if command == "hello":
            print(COMMANDS["hello"]())
            continue
        if command == "show":
            print(COMMANDS["show"]())
            continue
        if command == "wrong_command":
            print("Wrong command")
            continue
        print(COMMANDS[command](user_command))


if __name__ == "__main__":
    main()