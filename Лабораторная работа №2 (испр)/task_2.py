salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

month = 0 # считаем месяцы
budget = 0 # считаем деньги на это время

for month in range(months):
    budget += (spend - salary) # прибавляем разницу расходов и доходов в бюджет
    spend *= (1+increase) # ежемесячный рост цен

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(budget,2))
