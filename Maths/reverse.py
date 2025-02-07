import datetime

def calculate(date1, date2):
    date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
    delta = date2 - date1
    print(f"Різниця між датами: {delta.days} днів")

today = '2023-03-22'
set_date_str = '2023-04-15'
calculate(today, set_date_str)

from datetime import date, datetime

today = date.today()

print("Today's date:", today)
set_date = input("Введіть дату в форматі '2022-01-31':")

set_date_str = datetime.strptime(set_date, "%Y-%m-%d")
print(set_date_str)
today_str = datetime.today().strftime("%Y-%m-%d")


def calculate(date1,date2):
    for i in date1:
            yearsi = i.year
            year_delta = yearsi - date2.year
            months = i.month
            days = i.day
            print(f"You are  {year_delta} {months} {days}")
    return

calculate(today, set_date_str)


from datetime import date, datetime

today = date.today()

print("Today's date:", today)
set_date = input("Введіть дату в форматі '2022-01-31':")

set_date_str = datetime.strptime(set_date, "%Y-%m-%d")
today_str = datetime.today().strftime("%Y-%m-%d")
print(type(today_str))

def calculate(date1,date2):
    years = date1.year
    delta_y = years - date2.year
    mon = date1.month
    delta_m = date2.month - mon
    days = date1.day
    delta_d = date2.year - days
    return print(f"You are  {delta_y} {delta_m} {delta_d}")

calculate(today_str, set_date)