import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django

django.setup()

from pizzas.models import Pizza, Topping

# get all pizzas from the Pizza model
pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id)
    print(pizza)
    print(pizza.date_added)

p = Pizza.objects.get(id=1)
print(p.name)
print(p.date_added)

toppings = p.topping_set.all()

for t in toppings:
    print(t)
