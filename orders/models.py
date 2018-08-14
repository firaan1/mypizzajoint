from django.db import models

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

class SubExtra(models.Model):
    subextra = models.CharField(max_length = 64)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    def __str__(self):
        return f"Extra {self.subextra} cost ${self.price}"

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
    subchoice = models.CharField(max_length = 64)
    subsize = models.ForeignKey(Size, on_delete = models.CASCADE, related_name = "sub_size", blank = True, null = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    class Meta:
        unique_together = ["subchoice", "subsize"]
    def __str__(self):
        return f"{self.subchoice} subs ({self.subsize} sized) cost ${self.price}"

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
    dinnerplatterchoice = models.CharField(max_length = 64)
    dinnerplattersize = models.ForeignKey(Size, on_delete = models.CASCADE, related_name = "dinnerplatter_size")
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    def __str__(self):
        return f"{self.dinnerplattersize} sized {self.dinnerplatterchoice} cost ${self.price}"
