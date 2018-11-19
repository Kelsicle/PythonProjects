import datetime

def print_header():
    print('---------------------')
    print('     Birthday App')
    print('---------------------')
    print()

def get_birthday():
    print("When were you born? ")
    day = int(input("Day [DD]: "))
    month = int(input("Month [MM]: "))
    year = int(input("Year [YYYY]: "))

    bday = datetime.date(year, month, day)

    return bday


def compute_gap(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month,
                              original_date.day)

    dt = this_year - target_date
    return dt.days


def print_birthday(days):
    if days < 0:
        print("You had your birthday {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Happy Birthday!")


def main():
    print_header()
    bday = get_birthday()
    today = datetime.date.today()
    number_days = compute_gap(bday, today)
    print_birthday(number_days)


main()
