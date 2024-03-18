from Customer import Customer

class PersonCustomer(Customer):
    def __init__(self, name, birthday, cpf, address):
        super().__init__(address)
        self.name = name
        self.birthday = birthday
        self.cpf = cpf