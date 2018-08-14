from orders.models import *

size = ["Small", "Large"]
for s in size:
    ss = Size(size = s)
    ss.save()
    del(ss)

pizzatype = ["Regular", "Sicilian"]
for s in pizzatype:
    ss = PizzaType(pizzatype = s)
    ss.save()
    del(ss)

toppingtype = ["Cheese", "1 topping", "2 toppings", "3 toppings", "Special"]
for s in toppingtype:
    ss = ToppingType(toppingtype = s)
    ss.save()
    del(ss)

toppingchoice = ['Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 'Ham', 'Canadian Bacon', 'Pineapple', 'Eggplant', 'Tomato & Basil', 'Green Peppers', 'Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken', 'Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini']
for s in toppingchoice:
    ss = ToppingChoice(toppingchoice = s)
    ss.save()
    del(ss)

subextra = ['Mushrooms', 'Green Peppers', 'Onions', 'Extra Cheese']
price = '0.50'
for s in subextra:
    ss = SubExtra(subextra = s, price = price)
    ss.save()
    del(ss)

# adding pizzas
price = ["12.20","17.45","13.20","19.45","14.70","21.45","15.70","23.45","17.25","25.45","23.45","37.70","25.45","39.70","27.45","41.70","28.45","43.70","29.45","44.70"]
i = 0
for pizzatype in range(1,3):
    for toppingtype in range(1,6):
        for pizzasize in range(1,3):
            ss = PizzaRate(pizzatype = PizzaType.objects.get(pk = pizzatype), pizzasize = Size.objects.get(pk = pizzasize), toppingtype = ToppingType.objects.get(pk = toppingtype), price = price[i])
            ss.save()
            del(ss)
            i += 1

# adding subs
subs = ['Cheese', 'Italian', 'Ham + Cheese', 'Meatball', 'Tuna', 'Turkey', 'Chicken Parmigiana', 'Eggplant Parmigiana', 'Steak', 'Steak + Cheese', 'Hamburger', 'Cheeseburger', 'Fried Chicken', 'Veggie']

price = ["6.50", "6.50", "6.50", "6.50", "6.50", "7.50", "7.50", "6.50", "6.50", "6.95", "4.60", "5.10", "6.95", "6.95", "7.95", "7.95", "7.95", "7.95", "7.95", "8.50", "8.50", "7.95", "7.95", "8.50", "6.95", "7.45", "8.50", "8.50"]

i=0
for subsize in range(1,3):
    for sub in subs:
        ss = SubRate(subchoice = sub, subsize = Size.objects.get(pk = subsize), price = price[i])
        ss.save()
        del(ss)
        i += 1

# add "Sausage, Peppers & Onions" using UI

# adding pasta
pastas = ["Baked Ziti w/Mozzarella", "Baked Ziti w/Meatballs", "Baked Ziti w/Chicken"]
price = ["6.50", "8.75", "9.75"]
i = 0
for pasta in pastas:
    ss = PastaRate(pastachoice = pasta, price = price[i])
    ss.save()
    del(ss)
    i += 1

# adding salads
salads = ["Garden Salad", "Greek Salad", "Antipasto", "Salad w/Tuna"]
price = ["6.25", "8.25", "8.25", "8.25"]
i = 0
for salad in salads:
    p = SaladRate(saladchoice = pasta, price = price[i])
    p.save()
    del(p)
    i += 1

# adding dinnerplatter
platters = ["Garden Salad", "Greek Salad", "Antipasto", "Baked Ziti", "Meatball Parm", "Chicken Parm"]
price = ["35.00", "60.00", "45.00", "70.00", "45.00", "70.00", "35.00", "60.00", "45.00", "70.00", "45.00", "80.00"]
i = 0
for platter in platters:
    for plattersize in range(1,3):
        d = DinnerPlatterRate(dinnerplatterchoice = platter, dinnerplattersize = Size.objects.get(pk = plattersize), price = price[i])
        d.save()
        del(d)
        i += 1
