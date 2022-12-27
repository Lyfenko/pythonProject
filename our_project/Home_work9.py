Phonebook = {}

def input_error(func):

    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Please, enter the name and number"
        except ValueError:
            return "Enter a valid number"
        except KeyError:
            return "No such name in phonebook"

    return wrapper


def hello(*args):
    return "How can I help you?"


@input_error
def add(*args):
    name = args[0]
    phone = args[1]
    if name not in Phonebook:
        Phonebook[name] = phone
    else:
        return f"The name {name} already exists."
    return f"Contact {name} added successfully"

@input_error
def change_phone(*args):
    name = args[0]
    phone = args[1]
    if name in Phonebook:
        Phonebook[name] = phone
    else:
        return f"Please add {name} to phonebook firstly"
    return f"Contact {name} changed successfully"


@input_error
def phone(*args):
    return Phonebook[args[0]]

def show_all(*args):
    lst = ["{:^10}: {:>10}".format(k, v) for k, v in Phonebook.items()]
    return "\n".join(lst)


def end_work(*args):
    return "Good bye"



COMMANDS = {hello: ["hello", "hi"],
            change_phone: ["change"],
            phone: ["phone"],
            end_work: ["exit", "close", "good bye", ".", "bye"],
            add: ["add"],
            show_all: ["show all", "show"]
            }

def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, tuple(user_input[len(i):].strip().split(" "))


def main():
    while True:
        user_input = input(">>> ")
        try:
            result, data = parse_command(user_input)
            print(result(*data))
            if result is exit:
                break
        except TypeError:
            print("No such command")


if __name__ == "__main__":
    main()
