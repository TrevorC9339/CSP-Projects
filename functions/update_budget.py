from __future__ import division
from cmath import rect

def cost(type, varible):
    input("how much is your", type, varible)

def percent(type, amount):
    decimal = income/amount*100
    print("your", type, "is %", decimal, "of your income.", type, decimal)




print("This will calculate your budget")
income = input("What is your income?")
rent = cost("rent", rent)
utilities = cost("utilities")
groceries = cost("groceries", )
transport = cost("transport")
expenses = int(rent + utilities + transport + groceries)
savings = int(income-expenses)
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