import json
#1----------------------------------------------------------------------------------------------------------------------
user_lines = []

while True:
    user_input = str(input('Введите строку для записи или пустую строку чтобы завершить запись:'))
    if user_input == '':
        print('Запись завершена.')
        break
    user_lines.append(user_input + '\n')

with open('out_file.txt', 'w', encoding='utf-8') as file:
    file.writelines(user_lines)


#2----------------------------------------------------------------------------------------------------------------------
with open('testfile_2.txt') as file:
    lines = file.readlines()
with open('testfile_2.txt', 'r', encoding='utf-8') as file:
    for index, value in enumerate(lines):
        num_words = len(value.split())
        result = (f'Line #{index+1}: "{value}" has {num_words} word' + ('s' if num_words > 1 else '')).replace('\n', '')
        print(result)


#3----------------------------------------------------------------------------------------------------------------------
salaries = []
with open('employees.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
with open('employees.txt', 'r', encoding='utf-8') as file:
    for i in range(len(lines)):
        employee = lines[i].split()[0]
        salary = float(lines[i].split()[1])
        salaries.append(salary)
        if salary < 20000.00:
            print(f'Сотрудник {employee} имеет оклад ниже 20 тыс., а точнее {salary}')
print('Средняя величина дохода всех сотрудников =', sum(salaries) // len(salaries))


#4----------------------------------------------------------------------------------------------------------------------
with open('numbers.txt', 'r+', encoding='utf-8') as file, open('new_numbers.txt', 'w', encoding='utf-8') as new_file:
    for el in file:
        if 'One' in el:
            el = el.replace('One', 'Один')
        elif 'Two' in el:
            el = el.replace('Two', 'Два')
        elif 'Three' in el:
            el = el.replace('Three', 'Три')
        elif 'Four' in el:
            el = el.replace('Four', 'Четыре')
        print(el, end='', file=new_file)

#5----------------------------------------------------------------------------------------------------------------------
with open('sumnums.txt', 'w', encoding='utf-8') as file:
    for i in range(10):
        file.write(str(i) + ' ')
with open('sumnums.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.split()

line = [int(i) for i in line]
print('Сумма чисел в файле =', sum(line))


#6----------------------------------------------------------------------------------------------------------------------
with open('studies.txt', 'r+', encoding='utf-8') as file:
    names = []
    sums = []
    for line in file:
        line_list = line.split()
        names.append(line_list[0])
        result = 0
        for element in line_list[1:]:
            if '(' in element:
                element = element[0:element.index('(')]
                result += int(element)
        sums.append(result)

studies_dict = {names[i]:sums[i] for i in range(len(names))}
print(studies_dict)
#7----------------------------------------------------------------------------------------------------------------------
def calc_profit(revenue, costs):
    return revenue-costs

with open('firms_profits.txt', 'r+', encoding='utf-8') as file:
    names = []
    profits = []
    for line in file:
        line_list = line.split()
        company_name = line_list[0]
        company_profit = calc_profit(int(line_list[2]), int(line_list[3]))
        profits.append(company_profit)
        names.append(company_name)
avg_profit = int(sum([profit for profit in profits if profit > 0])/len([profit for profit in profits if profit > 0]))
result_list = [{names[i]:profits[i] for i in range(len(names))}, {'average_profit':avg_profit}]
print(result_list)

with open('firms_profits.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_list, json_file)

