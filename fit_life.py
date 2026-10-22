# Проект FitLife - MVP версия 1.0
import sys

sys.stdout.reconfigure(encoding="utf-8")


# 1. Знакомство
print('Привет! Я бот FitLife. Давай познакомимся.')
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
user_name = input('Как тебя зовут? ')
# TODO: Спроси возраст и сохрани в переменную user_age
user_age = int(input('Сколько тебе лет? '))

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
user_weight = float(input('Введи свой вес (в кг): '))
# TODO: Запроси рост (в метрах, например 1.75)
while True:
    try:
        user_height = float(input('Введи свой рост (в м, например, 1.75): '))
        if not (0.5 <= user_height <= 2.5):
            print('Ошибка: рост должен быть в диапазоне 0.5 м - 2.5 м')
            continue
        break
    except ValueError:
        print('Ошибка: нужно ввести число, например 1.75')


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)


# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
WATER_PER_KG = 30
ML_IN_L = 1000
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_L


# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие и данные
print(
    '',
    f'Отчёт для пользователя: {user_name} ({user_age} г.)',
    f'Твой Индекс Массы Тела: {bmi}',
    f'Рекомендуется нормы воды: {water_l:.1f} л в день',
    '',
    'Расчёт окончен. Будьте здоровы!', sep='\n'
)
