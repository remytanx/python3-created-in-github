# menu.py file

from typing import List
from pizzapy.pizza import Pizza

MENU: List[Pizza] = [
    Pizza('Margherita', 30, 10.0),
    Pizza('Carbonara', 45, 14.99),
    Pizza('Marinara', 35, 16.99),
    Pizza('Hawaiian',90,20.99),
]

if __name__ == '__main__':
    print(MENU)