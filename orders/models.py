from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import RegexValidator


# Create your models here.
class Size(models.Model):
    size = models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.size}"

class PizzaType(models.Model):
    pizzatype = models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.pizzatype}"

class ToppingType(models.Model):
    toppingtype = models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.toppingtype}"

class ToppingChoice(models.Model):
    toppingchoice = models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.toppingchoice}"

class SubChoice(models.Model):
    subchoice = models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.subchoice}"

class DinnerPlatterChoice(models.Model):
    dinnerplatterchoice = models.CharField(max_length = 64)
    def __str__(self):
        return f"{self.dinnerplatterchoice}"

class PizzaRate(models.Model):
    pizzatype = models.ForeignKey(PizzaType, on_delete = models.CASCADE, related_name = "pizza_type")
    pizzasize = models.ForeignKey(Size, on_delete = models.CASCADE, related_name = "pizza_size")
    toppingtype = models.ForeignKey(ToppingType, on_delete = models.CASCADE, related_name = "topping_type")
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    class Meta:
        unique_together = ["pizzatype", "pizzasize", "toppingtype"]
    def __str__(self):
        return f"{self.pizzasize} sized {self.pizzatype} pizza with {self.toppingtype} cost ${self.price}"

class SubRate(models.Model):
    subchoice = models.ForeignKey(SubChoice, on_delete = models.CASCADE, related_name = "sub_choice")
    subsize = models.ForeignKey(Size, on_delete = models.CASCADE, related_name = "sub_size", blank = True, null = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    class Meta:
        unique_together = ["subchoice", "subsize"]
    def __str__(self):
        return f"{self.subchoice} subs ({self.subsize} sized) cost ${self.price}"

class SubExtraRate(models.Model):
    subextrachoice = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    class Meta:
        unique_together = ["subextrachoice"]
    def __str__(self):
        return f"{self.subextrachoice}"

class PastaRate(models.Model):
    pastachoice = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    def __str__(self):
        return f"{self.pastachoice} pasta cost ${self.price}"

class SaladRate(models.Model):
    saladchoice = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    def __str__(self):
        return f"{self.saladchoice} pasta cost ${self.price}"

class DinnerPlatterRate(models.Model):
    dinnerplatterchoice = models.ForeignKey(DinnerPlatterChoice, on_delete = models.CASCADE, related_name = "dinnerplatter_choice")
    dinnerplattersize = models.ForeignKey(Size, on_delete = models.CASCADE, related_name = "dinnerplatter_size")
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    def __str__(self):
        return f"{self.dinnerplattersize} sized {self.dinnerplatterchoice} cost ${self.price}"

class OrderPizza(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = "pizza_user", null = True)
    menutype = models.CharField(max_length=25, default="pizza", editable="False")
    pizzachoice = models.ForeignKey(PizzaRate, on_delete = models.SET_NULL, related_name = "pizza_choice", null = True)
    toppingchoice = models.ManyToManyField(ToppingChoice, related_name = "pizza_topping")
    paid = models.BooleanField(default = False)
    def display_toppingchoice(self):
        return ", ".join(t.toppingchoice for t in self.toppingchoice.all())
    def test(self):
        return "xx"
    def __str__(self):
        return f"{self.user} : {self.pizzachoice} with {self.display_toppingchoice()}"

class OrderSub(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = "sub_user", null = True)
    menutype = models.CharField(max_length=25, default="sub", editable="False")
    subchoice = models.ForeignKey(SubRate, on_delete = models.SET_NULL, related_name = "sub_choice", null = True)
    subextrachoice = models.ManyToManyField(SubExtraRate, related_name = "subextra_choice")
    paid = models.BooleanField(default = False)
    def display_subchoice(self):
        return ", ".join(s.subextrachoice for s in self.subextrachoice.all())
    def __str__(self):
        return f"{self.user} : {self.subchoice} with {self.display_subchoice()}"

class OrderPasta(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = "pasta_user", null = True)
    menutype = models.CharField(max_length=25, default="pasta", editable="False")
    pastachoice = models.ForeignKey(PastaRate, on_delete = models.SET_NULL, related_name = "pasta_choice", null = True)
    paid = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.user} : {self.pastachoice}"

class OrderSalad(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = "salad_user", null = True)
    menutype = models.CharField(max_length=25, default="salad", editable="False")
    saladchoice = models.ForeignKey(SaladRate, on_delete = models.SET_NULL, related_name = "salad_choice", null = True)
    paid = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.user} : {self.saladchoice}"

class OrderDinnerPlatter(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = "dinnerplatter_user", null = True)
    menutype = models.CharField(max_length=25, default="dinnerplatter", editable="False")
    dinnerplatterchoice = models.ForeignKey(DinnerPlatterRate, on_delete = models.SET_NULL, related_name = "dinnerplatter_choice", null = True)
    paid = models.BooleanField(default = False)
    def __str__(self):
        return f"{self.user} : {self.dinnerplatterchoice}"

class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, related_name = "address_user")
    address = models.CharField(max_length = 1000)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    def __str__(self):
        return f"{self.address}, {self.phone_number}"

class PlacedOrder(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, related_name = "placedorder_user", null = True)
    deliveryaddress = models.ForeignKey(DeliveryAddress, on_delete = models.SET_NULL, null = True, related_name = "delivery_address")
    orderpizza = models.ManyToManyField(OrderPizza, related_name = "order_pizza", blank = True)
    ordersub =  models.ManyToManyField(OrderSub, related_name = "order_sub", blank = True)
    orderpasta = models.ManyToManyField(OrderPasta, related_name = "order_pasta", blank = True)
    ordersalad =  models.ManyToManyField(OrderSalad, related_name = "order_salad", blank = True)
    orderdinnerplatter =  models.ManyToManyField(OrderDinnerPlatter, related_name = "order_dinnerplatter", blank = True)
    totalprice =  models.DecimalField(max_digits = 6, decimal_places = 2, default = 0)
    datetime = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default = False)
    def clean(self):
        if not (self.orderpizza or self.ordersub or self.orderpasta or self.ordersalad or self.orderdinnerplatter):
            raise ValidationError("You must specify atleast one order")
    def __str__(self):
        count = 0
        for i in self.orderpizza, self.ordersub, self.orderpasta, self.ordersalad, self.orderdinnerplatter:
            if i:
                count += 1
        return f"{self.user}'s order at {self.datetime} to {self.deliveryaddress}; Order completed: {self.completed}"
