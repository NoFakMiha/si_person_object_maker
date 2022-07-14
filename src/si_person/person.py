import random
import data

class Person:

    def name(self):
        return random.choice(data.first_name)

    def last_name(self):
        return random.choice(data.last_name)

    def address(self):
        return f'{random.choice(data.street_names)} {random.randint(1,70)}'
    def zip_city(self):
        return  f'{random.choice(data.postal_code)} {random.choice(data.city)}'

