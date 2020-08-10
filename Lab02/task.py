import json
import random

def set_range(start, end):
    current = start 
    while current < end:
        yield current
        current += 1

id_pool = set_range(1,10000)

class Client:
    def __init__(self, first_name, last_name, age, balance=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.balance = balance
        self.id = next(id_pool)

    def __str__(self):
        return "Client {} {} with id {} age = {}, balance: ${}".format(self.first_name, self.last_name, self.id, self.age, self.balance)


class Bank:

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.client_list = []

    def add_client(self, newClient):
        self.client_list.append(newClient)

    def info(self):
        print(self.bank_name, ":\n")

        for client in self.client_list:
            print(json.dumps(client.__dict__, indent=4))
    
    def deposit(self, client, money_add):
        client.balance += money_add
        return True

    def withdraw(self, client, cash_request):
        if cash_request > client.balance:
            return None
        else:
            client.balance -= cash_request
            return cash_request

    def transfer_from_to(self, client, receiver, amount):
        if amount > client.balance:
            return False
        else:
            receiver.balance += amount
            client.balance -= amount
            return True
    
    def give_credit(self, client, amount):
        client.balance += amount
    
    
names = ['Ania', 'Hania', 'Alina', 'John', 'Ron', 'Harry', 'Larry']
surnames = ['Smith', 'Page', 'Apple', 'Kowalski', 'Spacey']

def generate_client():
    new_person = Client(random.choice(names),
                        random.choice(surnames),
                        random.randint(16, 99))
    return new_person


def generate_client_list(clients_number):
    L = []
    for i in range(clients_number):
        x = generate_client()
        L.append(x)
    
    return L

clients_list = generate_client_list(16)


def generate_bank(name, clients_number):
    new_bank = Bank(name)

    for i in range(clients_number):
        new_bank.add_client(clients_list.pop())

    new_bank.info()

    return new_bank


if __name__ == "__main__":

    xBank = generate_bank('zBank', 5)
    yBank = generate_bank('yBank', 2)

