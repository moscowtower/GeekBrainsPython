from sys import argv
def salary(hours, wage, reward):
    salary = (int(hours) * int(wage)) + int(reward)
    print(f'Расчет заработной платы исходя из: \n - ставки в {wage}$/час;\n - {hours} часов; \n - премии размером в {reward}$:')
    print(f'Зарплата = {salary}$')

try:
    script_name, hours, wage, reward = argv
    salary(hours, wage, reward)

except ValueError or NameError:
    print('Требуется три позиционных параметра — кол-во рабочих часов, почасовая ставка и размер премии')
