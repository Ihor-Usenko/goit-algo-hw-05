# from collections import UserDict


# class Field:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)


# class Name(Field):
#     pass


# class Phone(Field):
#     def __init__(self, value):
#         if not self.validate(value):
#             raise ValueError("Phone number must be 10 digits.")
#         super().__init__(value)

#     @staticmethod
#     def validate(value):
#         return value.isdigit() and len(value) == 10


# class Record:
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []

#     def add_phone(self, phone):
#         self.phones.append(Phone(phone))

#     def remove_phone(self, phone):
#         self.phones = [p for p in self.phones if p.value != phone]

#     def edit_phone(self, old_phone, new_phone):
#         for i, phone in enumerate(self.phones):
#             if phone.value == old_phone:
#                 self.phones[i] = Phone(new_phone)
#                 break

#     def find_phone(self, phone):
#         for p in self.phones:
#             if p.value == phone:
#                 return p
#         return None

#     def __str__(self):
#         return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


# class AddressBook(UserDict):
#     def add_record(self, record):
#         self.data[record.name.value] = record

#     def find(self, name):
#         return self.data.get(name)

#     def delete(self, name):
#         if name in self.data:
#             del self.data[name]


# book = AddressBook()
# john_record = Record('John')

# john_record.add_phone("5555555555")
# expert = Field('Igor')
# print(expert.value)
# book.add_record(john_record)
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)
# for k, v in book.data.items():
#     print(v)

class Dog:
    def speak(self):
        return "Woof"


class Cat():
    def speak(self):
        return "Meow"


class Robot():
    def speak(self):
        return "Beep"


def who_speak(speaker):
    print(speaker.speak())


dog = Dog()
cat = Cat()
robot = Robot()

who_speak(robot)
