Phonebook = {}

def input_error(func):

    def wrapper():
        try:
            return func()
        except IndexError:
            return "Give me name, old phone and new phone"
        except KeyError:
            return "Enter correct username"
        except ValueError:
            return "Enter username"
    return wrapper

def hello():
    return "How can I help you?"

def end_work():
    return "Good bye"

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
def add(name, phone_number):
    if name in Phonebook:
        Phonebook[name].append(modified_number(phone_number))
    if name not in Phonebook:
        Phonebook[name] = []
        Phonebook[name].append(modified_number(phone_number))
    return f"Add new contact - {name} {modified_number(phone_number)}"

@input_error
def change(name: str, old_number: str, new_number):
    if name in Phonebook:
        Phonebook[name].remove(modified_number(old_number))
        Phonebook[name].append(modified_number(new_number))
    return f"Change contact {name} - number {modified_number(old_number)} to number {modified_number(new_number)}"

@input_error
def phone(name):
    phones = ""
    for i in Phonebook[name]:
        phones += i + " "
    return phones

COMMANDS = {hello: ['hello', 'hi'],
            phone: ['phone'],
            add: ['add'],
            change: ['change'],
            end_work: ['.', 'bye', 'good bye', 'close', 'exit']
            }

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
    else:
        return "wronge_command"

def bot():
    while True:
        user_command = input(">> ")
        command = parser(user_command)
        if command == "end_work":
            print(COMMANDS["end_work"]())
            break
        if command == "hello":
            print(COMMANDS["hello"]())
            continue
        if command == "wrong_command":
            print("Wrong command")
            continue
        print(COMMANDS[command](user_command))


if __name__ == "__main__":
    bot()