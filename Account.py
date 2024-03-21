from History import History

class Account:
    def __init__(self, number, customer):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._customer = customer
        self._history = History()
    
    @classmethod
    def new_account(cls, customer, number):
        return cls(number, customer)
    @property
    def balance(self):
        return self._balance
    @property
    def number(self):
        return self._number
    @property
    def agency(self):
        return self._agency
    @property
    def customer(self):
        return self._customer
    @property
    def history(self):
        return self._history
    def withdraw(self, value):
        balance = self.balance
        exceeded_balance = value > balance

        if exceeded_balance:
            print("\n@@@ Operação falhou! Você nao tem saldo suficiente. @@@")
        elif value > 0:
            self._balance -= value
            print("\n=== Saque realizado com sucesso ===")
            return True
        else:
            print("\n@@@ Operação falhou! Valor informado é invalido. @@@")
        
        return False
    def deposit(self, value):
        if value > 0:
            self._balance += value
            print("\n=== Deposito realizado com sucesso ===")
        else:
            print("\n@@@ Operação falhou! Valor informado é invalido. @@@")
            return False
        return True


            


