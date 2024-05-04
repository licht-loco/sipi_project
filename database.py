import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('schedule.db')
cursor = conn.cursor()

# Создаем таблицу расписания, если она не существует
def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS schedule (
                        id INTEGER PRIMARY KEY,
                        day TEXT,
                        subject TEXT,
                        time TEXT
                    )''')
    conn.commit()

# Заполнение таблицы расписания администратором
def add_schedule(day, subject, time):
    cursor.execute('''INSERT INTO schedule (day, subject, time) VALUES (?, ?, ?)''', (day, subject, time))
    conn.commit()

# Получение расписания по дням
def get_schedule(day):
    cursor.execute('''SELECT subject, time FROM schedule WHERE day=?''', (day,))
    rows = cursor.fetchall()
    return rows
