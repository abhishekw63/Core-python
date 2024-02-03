class MinimumBalance(Exception):
    pass

class Bank:
    account_number=1001

    def __init__(self,name,balance):
        try:
            if balance<1000:
                raise MinimumBalance("Minimum Balance 1000 required.")
            self.name=name
            self.bal=balance
            self.acc_num=Bank.account_number
            Bank.account_number+=1
        except MinimumBalance as err:
            print(err)
        
    def deposit(self,amount):
        self.bal+=amount

    def withdraw(self,withdr):
            try:
                if self.bal-withdr<1000:
                    raise MinimumBalance("Balance falls below 1000")
                self.bal-=withdr
            except MinimumBalance as err:
                print(err)
    def show(self):
            print(f'Name:{self.name} Account number:{self.acc_num} Balance:{self.bal} ')


abhi=Bank('abhishek',10000)
abhi.show()

raj=Bank('Raj',5000)
raj.withdraw(450)   
raj.deposit(450)
raj.show()        