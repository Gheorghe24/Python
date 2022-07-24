import csv
from sys import float_info


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('/mnt/d/Python/OOP_tutorial/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # ex 10.0 5.0

        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity}) "


class Phone(Item):
    # all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0) -> None:
        #Call to super function to have access to all atributes/ methods
        super().__init__(name, price, quantity)
        # Run validation to the received arguments
        
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than zero"

        # Assign to self object
        self.broken_phones = broken_phones

        # Actions to execute
        # Phone.all.append(self)


phone1 = Phone("iPHONE10", 500, 10,1)
print(phone1.calculate_total_price())
phone2 = Item("iPHONE9", 300, 10)

print(Item.all)
print(Phone.all)
