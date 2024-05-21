from datetime import datetime, date


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append(
            {"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    for i in users:
        this_year_date = i['birthday'].replace(year=today.year)
        res = this_year_date - today
        if res.days > 0 and res.days < 7:
            i['birthday'] = date_to_string(this_year_date)
            change_name_key = i.pop('birthday')
            i['congratulation_date'] = change_name_key
            upcoming_birthdays.append(i)
    return upcoming_birthdays
