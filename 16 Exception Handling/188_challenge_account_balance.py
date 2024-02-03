class AccountBalanceException(Exception): #dummy class inheriting from exception
    pass

def withdraw(amount):
    global balance #what is need of writing global here?
    if balance-amount<5000:
        raise AccountBalanceException('Minimum balance 5000 is not maintained')
    else:
        balance-=amount
        print("your balance is:",balance)

balance=10000

try:
    withdraw(6000)
except AccountBalanceException as e:
    print(e)