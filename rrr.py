from datetime import datetime, date


def string_to_date(date_string):
    return datetime.strptime(date_string, "%d.%m.%Y").date()


print(string_to_date('30.04.1970'))
