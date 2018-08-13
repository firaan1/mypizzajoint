from orders.models import Attr, PizzaRate

size = ["Small", "Large"]
pizzatype = ["Regular", "Sicilian"]
toppingtype = ["Cheese", "1 topping", "2 toppings", "3 toppings", "Special"]

toppings = ['Pepperoni', 'Sausage', 'Mushrooms', 'Onions', 'Ham', 'Canadian Bacon', 'Pineapple', 'Eggplant', 'Tomato & Basil', 'Green Peppers', 'Hamburger', 'Spinach', 'Artichoke', 'Buffalo Chicken', 'Barbecue Chicken', 'Anchovies', 'Black Olives', 'Fresh Garlic', 'Zucchini']
]
for t in toppings:
    tt = Attr(field = "Topping", value = t)
    tt.save()
    del(tt)

price = ["12.20","17.45","13.20","19.45","14.70","21.45","15.70","23.45","17.25","25.45","23.45","37.70","25.45","39.70","27.45","41.70","28.45","43.70","29.45","44.70"]
i=0
for pizzatype in [Attr.objects.get(id = '4'), Attr.objects.get(id = '5')]:
    for toppingtype in [Attr.objects.get(id = '6'), Attr.objects.get(id = '7'), Attr.objects.get(id = '8'), Attr.objects.get(id = '9'), Attr.objects.get(id = '10')]:
        for pizzasize in [Attr.objects.get(id = '1'), Attr.objects.get(id = 2)]:
            print(f"{pizzatype} {pizzasize} {toppingtype} {price[i]}")
            pp = PizzaRate(PizzaType = pizzatype, PizzaSize = pizzasize, ToppingType = toppingtype, Price = price[i])
            pp.save()
            del(pp)
            i += 1


# Attr
substype = ["main", "extra"]
i = 0
for e in substype:
    e1 = Attr(field = "SubsType", value = e)
    e1.save()
    del(e1)
    i += 1

# Subs
subs = ['Cheese', 'Italian', 'Ham + Cheese', 'Meatball', 'Tuna', 'Turkey', 'Chicken Parmigiana', 'Eggplant Parmigiana', 'Steak', 'Steak + Cheese', 'Hamburger', 'Cheeseburger', 'Fried Chicken', 'Veggie']

price = ["6.50", "6.50", "6.50", "6.50", "6.50", "7.50", "7.50", "6.50", "6.50", "6.95", "4.60", "5.10", "6.95", "6.95", "7.95", "7.95", "7.95", "7.95", "7.95", "8.50", "8.50", "7.95", "7.95", "8.50", "6.95", "7.45", "8.50", "8.50"]

i=0
for subssize in [Attr.objects.get(id = '1'), Attr.objects.get(id = 2)]:
    for sub in subs:
        ss = SubsRate(SubsType = Attr.objects.get(id = '34'), SubsChoice = sub, SubsSize = subssize, Price = price[i])
        ss.save()
        del(ss)
        i += 1

extras = ['Mushrooms', 'Green Peppers', 'Onions', 'Extra Cheese']
price = '0.50'
i=0
for subssize in [Attr.objects.get(id = '1'), Attr.objects.get(id = 2)]:
    for extra in extras:
        s1 = SubsRate(SubsType = Attr.objects.get(id = '35'), SubsChoice = extra, SubsSize = subssize, Price = price)
        s1.save()
        del(s1)
        i += 1

s2 = SubsRate(SubsType = Attr.objects.get(id = '34'), SubsChoice = "Sausage, Peppers & Onions", SubsSize = Attr.objects.get(id = '3'), Price = "8.50")
s2.save()
del(s2)

# pasta
pastas = ["Baked Ziti w/Mozzarella", "Baked Ziti w/Meatballs", "Baked Ziti w/Chicken"]
price = ["6.50", "8.75", "9.75"]
i = 0
for pasta in pastas:
    p = PastaRate(PastaChoice = pasta, Price = price[i])
    p.save()
    del(p)
    i += 1

# salad
salads = ["Garden Salad", "Greek Salad", "Antipasto", "Salad w/Tuna"]
price = ["6.25", "8.25", "8.25", "8.25"]
i = 0
for salad in salads:
    p = SaladsRate(SaladsChoice = pasta, Price = price[i])
    p.save()
    del(p)
    i += 1

# dinner platter
platters = ["Garden Salad", "Greek Salad", "Antipasto", "Baked Ziti", "Meatball Parm", "Chicken Parm"]
price = ["35.00", "60.00", "45.00", "70.00", "45.00", "70.00", "35.00", "60.00", "45.00", "70.00", "45.00", "80.00"]
i = 0
for platter in platters:
    for plattersize in [Attr.objects.get(id = '1'), Attr.objects.get(id = 2)]:
        d = DinnerPlattersRate(DinnerPlattersChoice = platter, DinnerPlattersSize = plattersize, Price = price[i])
        d.save()
        del(d)
        i += 1
