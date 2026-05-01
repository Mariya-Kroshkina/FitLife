# Проект FitLife - MVP версия 1.0
import constants

# приветствуем пользователя и выясняем необходимые данные
print('Привет, меня зовут FitLife бот')

user_name = input('А как тебя зовут? ').title()
print()
print(f'Приятно познакомиться, {user_name}.')

print('Мне необходимо узнать некоторые твои параметры,', end=' ')
print('чтобы правильно составить рекомендации.')

while True:
    try:
        age = int(input('Подскажи, пожалуйста, свой возраст. '))
        print('Отлично! Я могу расчитать индекс массы тела (ИМТ)', end=' ')
        print('и норму воды для тебя.')
        break
    except ValueError:
        print('Ошибка! Нужно ввести целое число. Попробуй ещё раз.')

print('Для этого мне необходимо узнать твой вес в КГ.')
user_weight = float(input('Напиши его здесь. ').replace(',', '.'))
user_height = float(input('Напиши, пожалуйста, мне свой рост в метрах. ').replace(',', '.'))


# считаем индекс массы тела и округляем
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# считаем норму воды в мл
water_ml = user_weight * constants.WATER_PER_KG
# переводим норму воды в мл в л
water_ml = water_ml / constants.MILLILITER_IN_LITER

# Выводим данные
print()
print(f'Отчет для пользователя: {user_name} ({age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_ml:.1f} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
