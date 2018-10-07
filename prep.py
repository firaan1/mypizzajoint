# Sorry, this is a bit messy
from orders.models import *

size = ["Small", "Large"]
if Size.objects.count() > 0:
    print("Size table is not empty ... skipping")
else:
    print("Adding pizza size")
    for s in size:
        print(f"{s}")
        ss = Size(size = s)
        ss.save()
        del(ss)

pizzatype = ["Regular", "Sicilian"]
if PizzaType.objects.count() > 0:
    print("PizzaType table is not empty ... skipping")
else:
    print("Adding pizza type")
    for s in pizzatype:
        print(f"{s}")
        ss = PizzaType(pizzatype = s)
        ss.save()
        del(ss)

toppingtype = ["Cheese", "1 topping", "2 toppings", "3 toppings", "Special"]
if ToppingType.objects.count() > 0:
    print("ToppingType table is not empty ... skipping")
else:
    print("Adding pizza topping type")
    for s in toppingtype:
        print(f"{s}")
        ss = ToppingType(toppingtype = s)
        ss.save()
        del(ss)

toppingchoice = ['Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 'Ham', 'Canadian Bacon', 'Pineapple', 'Eggplant', 'Tomato & Basil', 'Green Peppers', 'Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken', 'Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini']
if ToppingChoice.objects.count() > 0:
    print("ToppingChoice table is not empty ... skipping")
else:
    print("Adding pizza topping choice")
    for s in toppingchoice:
        print(f"{s}")
        ss = ToppingChoice(toppingchoice = s)
        ss.save()
        del(ss)


# adding pizzas
price = ["12.20","17.45","13.20","19.45","14.70","21.45","15.70","23.45","17.25","25.45","23.45","37.70","25.45","39.70","27.45","41.70","28.45","43.70","29.45","44.70"]
if PizzaRate.objects.count() > 0:
    print("PizzaRate is not empty ... skipping")
else:
    print("Adding pizza rate")
    i = 0
    for pizzatype in range(1,3):
        for toppingtype in range(1,6):
            for pizzasize in range(1,3):
                print(f"{pizzasize} {pizzatype} pizza with {toppingtype} cost ${price[i]}")
                ss = PizzaRate(pizzatype = PizzaType.objects.get(pk = pizzatype), pizzasize = Size.objects.get(pk = pizzasize), toppingtype = ToppingType.objects.get(pk = toppingtype), price = price[i])
                ss.save()
                del(ss)
                i += 1

# addin subs
subs = ['Cheese', 'Italian', 'Ham + Cheese', 'Meatball', 'Tuna', 'Turkey', 'Chicken Parmigiana', 'Eggplant Parmigiana', 'Steak', 'Steak + Cheese', 'Hamburger', 'Cheeseburger', 'Fried Chicken', 'Veggie']
if SubChoice.objects.count() > 0:
    print("SubChoice table is not empty ... skipping")
else:
    print("Adding subs")
    for sub in subs:
        print(f"{sub}")
        ss = SubChoice(subchoice = sub)
        ss.save()
        del(ss)

price = ["6.50", "6.50", "6.50", "6.50", "6.50", "7.50", "7.50", "6.50", "6.50", "6.95", "4.60", "5.10", "6.95", "6.95", "7.95", "7.95", "7.95", "7.95", "7.95", "8.50", "8.50", "7.95", "7.95", "8.50", "6.95", "7.45", "8.50", "8.50"]
if SubRate.objects.count() > 0:
    print("SubRate table is not empty")
else:
    print("Adding subs rate")
    i=0
    for sub in range(1,len(SubChoice.objects.all()) + 1):
        for size in range(1, len(Size.objects.all()) + 1):
            print(f"{size} {sub} cost {price[i]}")
            ss = SubRate(subchoice = SubChoice.objects.get(pk = sub), subsize = Size.objects.get(pk = size), price = price[i])
            ss.save()
            del(ss)
            i += 1

subextras = ['Mushrooms', 'Green Peppers', 'Onions', 'Extra Cheese']
if SubExtraRate.objects.count() > 0:
    print("SubExtraRate table is not empty ... skipping")
else:
    print("Adding subs extras")
    price = "0.50"
    for subextra in subextras:
        print(f"{subextra}")
        ss = SubExtraRate(subextrachoice = subextra, price = price)
        ss.save()
        del(ss)

# adding pasta
pastas = ["Baked Ziti w/Mozzarella", "Baked Ziti w/Meatballs", "Baked Ziti w/Chicken"]
price = ["6.50", "8.75", "9.75"]
if PastaRate.objects.count() > 0:
    print("PastaRate table is not empty ... skipping")
else:
    print("Adding pasta")
    i = 0
    for pasta in pastas:
        print(f"{pasta}")
        ss = PastaRate(pastachoice = pasta, price = price[i])
        ss.save()
        del(ss)
        i += 1

# adding salads
salads = ["Garden Salad", "Greek Salad", "Antipasto", "Salad w/Tuna"]
price = ["6.25", "8.25", "8.25", "8.25"]
if SaladRate.objects.count() > 0:
    print("SaladRate table is not empty ... skipping")
else:
    print("Adding salads")
    i = 0
    for salad in salads:
        print(f"{salad}")
        p = SaladRate(saladchoice = salad, price = price[i])
        p.save()
        del(p)
        i += 1

# adding dinnerplatter
platters = ["Garden Salad", "Greek Salad", "Antipasto", "Baked Ziti", "Meatball Parm", "Chicken Parm"]
price = ["35.00", "60.00", "45.00", "70.00", "45.00", "70.00", "35.00", "60.00", "45.00", "70.00", "45.00", "80.00"]
if DinnerPlatterChoice.objects.count() > 0:
    print("DinnerPlatterChoice table is not empty ... skipping")
else:
    print("Adding dinner platters")
    for platter in platters:
        print(f"{platter}")
        d = DinnerPlatterChoice(dinnerplatterchoice = platter)
        d.save()
        del(d)

if DinnerPlatterRate.objects.count() > 0:
    print("DinnerPlatterRate table is not empty ... skipping")
else:
    i=0
    print("Adding dinner platter rates")
    for platterchoice in range(1,7):
        for plattersize in range(1,3):
            print(f"{plattersize} {platterchoice} cost {price[i]}")
            d = DinnerPlatterRate(dinnerplatterchoice = DinnerPlatterChoice.objects.get(pk = platterchoice), dinnerplattersize = Size.objects.get(pk = plattersize), price = price[i])
            d.save()
            del(d)
            i += 1
