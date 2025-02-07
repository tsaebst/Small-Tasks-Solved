import random
import datetime
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
while True:
    response = input('Скільки днів Ви хочете згенерувати?')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
def get_birthdays(number):
    birthdays = []
    for i in range(number):
        start = datetime.date(2000, 1, 1)
        random_days = datetime.timedelta(random.randint(0, 364))
        birthday = start + random_days
        birthdays.append(birthday)
    return birthdays

def run_experiment(birthdays):
    for i, x in enumerate(birthdays):
        if i >= len(birthdays) - 1:
            break
        for j, y in enumerate(birthdays[i + 1:]):
            if x == y:
                return x
    return None

def getMatch(birthdays):
      if len(birthdays) == len(set(birthdays)):
          return None

      for x, keyX in enumerate(birthdays):
        for y, keyY in enumerate(birthdays[x + 1:]):
             if keyX == keyY:
                  return keyX
print( numBDays, 'днів народження:')

birthdays = get_birthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(" ", end="")
        monthName = months[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText)

matches = getMatch(birthdays)

if matches != None:
    monthName = months[matches.month - 1]
    dateText = '{} {}'.format(monthName, matches.day)
    print('однакові дати днів народження', dateText)
else:
    print('Жодних збігів')
print('Згенеруємо', numBDays, 'дат 100000 разів')

simMatch = 0
for i in range(100000):
    if i % 10000 == 0:
        print(i, 'симуляцій проведено')
    birthdays = get_birthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100000 симуляцій завершено')
probability = round(simMatch / 100000 * 100)
print('вірогідність ', probability, '%')












