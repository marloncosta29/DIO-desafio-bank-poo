from Transaction import Transaction
from Account import Account

class Deposit(Transaction):
    def __init__(self, value):
        self._value = value
    
    @property
    def valor(self):
        return self._4
    
    def register(self, account: Account):
        success_transaction = account.deposit(self.value)

        if success_transaction:
            account.history.add_transaction(self=self)