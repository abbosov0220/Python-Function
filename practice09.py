def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        return "Yetarli mablag' yo'q"

def check_balance(balance):
    return balance

balance = 1000
balance = deposit(balance, 500)  
print("Balans:", check_balance(balance))

balance = withdraw(balance, 700) 
print("Balans:", check_balance(balance))

balance = withdraw(balance, 1000) 
print(balance)
