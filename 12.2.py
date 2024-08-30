import time


class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'{self.name}, price: {self.price}'


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'{self.name} {self.surname}'


class Purchase:
    @staticmethod
    def generate_id():
        current_time_millis = int(time.time() * 1000)
        unique_id = hex(current_time_millis)[2:]
        return unique_id

    def __init__(self, user):
        self.purchase_id = Purchase.generate_id()
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, qnt):
        if item in self.products:
            self.products[item] += qnt
        else:
            self.products[item] = qnt
        self.total += item.price * qnt

    def del_item(self, item, qnt):
        if item in self.products:
            if self.products[item] >= qnt:
                self.products[item] -= qnt
                self.total -= item.price * qnt
                if self.products[item] <= 0:
                    del self.products[item]

    def __str__(self):
        items_str = "\n".join(f'{item.name}: {qnt} pcs.' for item, qnt in self.products.items())
        return (f'"""\n'
                f'User: {self.user.name} {self.user.surname}\n'
                f'Items:\n'
                f'{items_str}\n'
                f'"""')

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


