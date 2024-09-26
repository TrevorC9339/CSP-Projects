from __future__ import division


def cost(type,):
    input("how much is your", type)

def percent(type, amount):
    decimal = income/amount*100
    print("your", type, "is %", decimal, "of your income.", type, decimal)




print("This will calculate your budget:")
income = int(input("how much do you make a month:"))
rent = int(input("how much do you pay in rent a month:"))
utilities = int(input("How much do you pay for utilities per month:"))
groceries = int(input("How much do you pay for grocieries a month:"))
transport = int(input("How much do you pay for transportation per month:"))
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