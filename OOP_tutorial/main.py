from item import Item
from phone import Phone

phone1 = Phone("iPHONE10", 500, 10,1)
print(phone1.calculate_total_price())
phone2 = Item("iPHONE9", 300, 10)

print(Item.all)
print(Phone.all)
