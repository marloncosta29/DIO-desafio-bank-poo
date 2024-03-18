from Account import Account
from Withdraw import Withdraw
class CurrentAccount(Account):
    def __init__(self, number, customer, limit = 500, withdraw_limit = 3):
        super().__init__(number, customer)
        self._limit = limit
        self._withdraw_limit = withdraw_limit
    def withdraw(self, value):
        withdraw_counts = len(
            [transaction for transaction in self.history.transactions if transaction['tipo'] == Withdraw.__name__]
        )

        exceeded_limit = value > self._limit
        exceeded_withdraw = withdraw_counts >= self._withdraw_limit

        if exceeded_limit:
            print("\n@@@ Operação falhou! O valor do saque excedeu o limite @@@")
        elif  exceeded_withdraw:
            print("\n@@@ Operação falhou! o limite de saques foi excedido @@@")
        else:
            return super().withdraw(value=value)
        return False
    def __str__(self) -> str:
        return f"""\
                Agencia:\t{self.agency}
                C/C:\t\t{self.number}
                Ttular:\t{self.customer.name}
                """