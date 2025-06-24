import pulp

# Створюємо задачу максимізації
model = pulp.LpProblem("Maximize_Total_Production", pulp.LpMaximize)

# Змінні рішення: кількість виробленого Лимонаду (L) та Фруктового соку (F)
L = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
F = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Цільова функція: максимізуємо загальну кількість продуктів
model += L + F, "Total_Products"

# Обмеження на ресурси
model += 2*L + 1*F <= 100, "Water_Constraint"
model += 1*L <= 50, "Sugar_Constraint"
model += 1*L <= 30, "Lemon_Juice_Constraint"
model += 2*F <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
model.solve()

# Вивід результатів
print("Статус:", pulp.LpStatus[model.status])
print("Кількість Лимонаду:", int(L.varValue))
print("Кількість Фруктового соку:", int(F.varValue))
print("Максимальна кількість продуктів:", int(pulp.value(model.objective)))
