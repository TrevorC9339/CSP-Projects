

def cost(int):
    int = input("how much is your " + int)
    return int

def percent(type, amount):
    decimal = income/amount*100
    print("your", type, "is %", amount, "of your income.")

print("This will calculate your budget")
income = cost("income")
rent = cost("rent")
utilities = cost("utilities")
groceries = cost("groceries")
transport = cost("transport")
expenses = int(rent + utilities + transport + groceries)
savings = int(income - expenses)
total = (int(income) - int(expenses))
print("your income is: $", income)
print("your expenses is: $", expenses)
print("your savings is: $", savings)
percent("rent", rent)
percent("utilities", utilities)
percent("transport", transport)
percent("expenses", expenses)
print("your expenses is: $", total)
print("Your monthly savings/spending money is: $", savings)