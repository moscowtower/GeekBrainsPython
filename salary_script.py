from sys import argv

script_name, hours, wage, reward = argv
salary = (int(hours)*int(wage)) + int(reward)
print(f'Расчет заработной платы исходя из: \n - ставки в {wage}$/час;\n - {hours} часов; \n - премии размером в {reward}$:')
print(f'Зарплата = {salary}$')