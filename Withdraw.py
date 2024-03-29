from Transaction import Transaction
from Account import Account

class Withdraw(Transaction):
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    def register(self, account: Account):
        success_transaction = account.withdraw(self.value)

        if success_transaction:
            account.history.add_transaction(self)