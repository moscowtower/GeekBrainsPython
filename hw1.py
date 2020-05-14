#1
first = 'I am the first variable'
second = f'Je suis le {len(first) if len(first)==2 else "deuxieme" } variable'
try:
    third = int(input("Input the third variable, ensure that it is an integer: "))
except ValueError:
    print('You failed to input an integer, wow')
    third = None
fourth = input("Input the fourth variable, ensure that it is a string: ")

print(first, ",", second, ",", third, ",", fourth)

#2
time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")

#3
n = input("Input an integer: ")
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n+n) + int(n+n+n)}")

#4
# Эх жаль так нельзя :(
# n = list(input("Input an integer: "))
# while True:
#    print(max(n))
#    break
n = int(input("Input an integer: "))
max = 0
while n > 0:
    if n % 10 == 9:
        max = 9
        break
    if n % 10 > max:
        max = n % 10
    n = n // 10
print(max)

#5
revenue = int(input("Input the profit of your company: "))
costs = int(input("Input the costs of your company: "))

profit = revenue - costs

if profit > 0:
    print("Congratulations! You've made a profit!")
    print(f"The rentability of your profit is: {revenue // costs}%")
    employees = int(input("Mind telling me how many employees you've got?: "))
    print(f"If you shared the profit equally among your workers, everyone would get {profit/employees}")
elif profit == 0:
    print("Breaking even is also a form of success! Keep going!")
else:
    print("A difference between a Master and a Beginner, is that the Master has failed more times, \n"
          "than the Beginner has even tried")

#6
first = int(input("Input the result of the first day (km): "))
result = int(input("Input the result of the day you're interested in (km): "))

def find(a, b):
    days = 1
    while a < b:
        a += a*0.1
        days +=1
    return days

print(f"На {find(first, result}}-й день спортсмен достиг результата - не менее {result} км.")
#