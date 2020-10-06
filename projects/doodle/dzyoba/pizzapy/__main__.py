# pizzapy/__main__.py

from pizzapy.menu import MENU

print('Awesomeness of pizza:')
for pizza in MENU:
    print(pizza.name, pizza.awesomeness())