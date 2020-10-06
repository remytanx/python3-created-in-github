# pizzashop/__main__.py

from pizzapy.menu import MENU

print('Shop Menu')
for pizza in MENU:
    print(pizza.name, pizza.awesomeness())
