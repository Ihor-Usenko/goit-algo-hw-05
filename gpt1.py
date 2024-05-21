from collections import UserDict
from datetime import datetime, date, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

    @staticmethod
    def validate(value):
        return value.isdigit() and len(value) == 10


class Birthday(Field):
    def __init__(self, value):
        if not self.validate(value):
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)

    @staticmethod
    def validate(value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
            return True
        except ValueError:
            return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        birthday_str = self.birthday.value if self.birthday else 'N/A'
        phones_str = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
        for record in self.data.values():
            if record.birthday:
                bday_date = datetime.strptime(
                    record.birthday.value, '%d.%m.%Y').date()
                this_year_bday = bday_date.replace(year=today.year)
                days_until_birthday = (this_year_bday - today).days
                if 0 < days_until_birthday <= days:
                    upcoming_birthdays.append(record)
        return upcoming_birthdays

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
        for i in self.data.values():
            this_year_date = i['birthday'].replace(year=today.year)
            res = this_year_date - today
            if res.days > 0 and res.days < 7:
                i['birthday'] = date_to_string(this_year_date)
                change_name_key = i.pop('birthday')
                i['congratulation_date'] = change_name_key
                upcoming_birthdays.append(i)
        return upcoming_birthdays


# Example usage:
ab = AddressBook()
r1 = Record("John Doe")
r1.add_phone("1234567890")
r1.add_birthday("15.06.1990")
ab.add_record(r1)

r2 = Record("Jane Doe")
r2.add_phone("0987654321")
r2.add_birthday("20.05.1985")
ab.add_record(r2)

upcoming_birthdays = ab.get_upcoming_birthdays()
for record in upcoming_birthdays:
    print(record)
