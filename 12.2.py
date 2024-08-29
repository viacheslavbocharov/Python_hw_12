import time
class Item:

    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions


    def __str__(self):
        return(f'Item information:\n'
              f'\tname: {self.name}\n'
              f'\tprice: {self.price}\n'
              f'\tdescription: {self.description}\n'
              f'\tdimensions: {self.dimensions}\n'
              f'___________________________________\n')

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return(f'User information:\n'
              f'\tname: {self.name}\n'
              f'\tsurname: {self.surname}\n'
              f'\tphonenumber: {self.numberphone}\n'
              f'___________________________________\n')

class Purchase:
    @staticmethod
    def generate_id():
        current_time_millis = int(time.time() * 1000)
        unique_id = hex(current_time_millis)[2:]
        return unique_id

    def __init__(self, user):
        self.purchase_id = Purchase.generate_id()
        self.products = {}
        self.name = user.name
        self.surname = user.surname
        self.total = 0

    def add_item(self, item, qnt):
        self.products[item.name] = qnt
        self.total += item.price * qnt

    def del_item(self, item, qnt):
        if item.name in self.products:
            if self.products[item.name] >= qnt:
                self.products[item.name] -= qnt
                self.total -= item.price * qnt
                if self.products[item.name] <= 0:
                    del self.products[item.name]

    def __str__(self):
        items_str = "\n".join(f'{name}: {qnt} pcs.' for name, qnt in self.products.items())
        return(f'Cart information:\n\n'
               f'User: {self.name} {self.surname}\n'
               f'Items:\n'
               f'{items_str}\n'
               f'___________________________________\n'
               )

    def get_total(self):
        return self.total


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item( 'apple', 2, "red", "middle", )
buyer = User("Ivan", "Ivanov", "02628162")
print(lemon)
print(apple)
print(buyer)

cart = Purchase(buyer)

cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
print(cart.get_total())

cart.del_item(lemon, 4)
cart.del_item(apple, 10)
print(cart)
print(cart.get_total())

cart.add_item(lemon, 1)
print(cart)
print(cart.get_total())


