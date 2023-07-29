from datetime import datetime, timedelta
def get_birthdays_per_week(users):
    
    # Отримуємо поточну дату
    current_date = datetime.now()
    # Знаходимо дату наступного понеділка
    next_monday = current_date + timedelta(days=(7 - current_date.weekday()))
    
    birthdays_by_day = {} # словник, де ключ - день тижня, а значення - список імен користувачів

    # Проходимося по кожному користувачу в списку
    for user in users:
        birthday = user['birthday'] # день народження користувача
        if current_date < birthday < next_monday + timedelta(days=7): # Перевіряємо, чи день народження припадає на наступний тиждень
            # Знаходимо день тижня для дня народження
            birthday_weekday = birthday.strftime('%A')

            # Якщо день народження припадає на суботу або неділю, то привітати потрібно в понеділок
            if birthday_weekday in ['Saturday', 'Sunday']:
                birthday_weekday = 'Monday'

            # Додаємо користувача до відповідного дня тижня в словнику
            birthdays_by_day.update({birthday_weekday: birthdays_by_day.get(birthday_weekday, []) + [user['name']]})
            
    # Впорядковуємо словник за днями тижня
    sorted_birthdays = sorted(birthdays_by_day.items(), key=lambda x: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'].index(x[0]))

    # Виводимо результат у вказаному форматі
    for weekday, names in sorted_birthdays:
        print(f"{weekday}: {', '.join(names)}")
    
    
    
users = [
    {'name': 'Ann', 'birthday': datetime(year=2023, month=8, day=4)},
    {'name': 'Bill', 'birthday': datetime(year=2023, month=7, day=30)},
    {'name': 'Alex', 'birthday': datetime(year=2023, month=7, day=31)},
    {'name': 'Bella', 'birthday': datetime(year=2023, month=8, day=1)}
    ]



def main():
    get_birthdays_per_week(users)


if __name__ == '__main__':
    main()

