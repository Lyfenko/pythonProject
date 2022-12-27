from collections import UserDict

class Field:
    def __init__(self,value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    @staticmethod
    def modification_phone_number(phone_user):
        new_phone = (
            phone_user.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        return new_phone

    def __init__(self, phone):
        modification_phone_number = Phone.modification_phone_number(phone)
        super().__init__(modification_phone_number)

class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if isinstance(phone, Phone):
            self.phones.append(phone)

    def show_contact(self):
        return {"name": self.name, "phone": self.phones}

    def add_phone(self, phone):
        self.phone.append(phone)

    def change_phone(self, phone):
        self.phones = phone

    def del_phone(self):
        self.phones = []

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def remove_record(self, record):
        self.data.pop(record.name.value, None)

    def show_records(self):
        return self.data

Phonebook = AddressBook()

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
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')