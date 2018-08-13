from django.db import models

# Create your models here.
class Attr(models.Model):
    field = models.CharField(max_length=25)
    value = models.CharField(max_length=64)

    def __str__(self):
        # return f"{self.value}"
        return f"{self.field}: {self.value}"

pizzatype_attr = Attr.objects.filter(field = "PizzaType").values('pk')
pizzasize_attr = Attr.objects.filter(field = "Size").exclude(id__in = Attr.objects.filter(field = "Size", value = "None").values('pk')).values('pk')
toppingtype_attr = Attr.objects.filter(field = "ToppingType").values('pk')
substype_attr = Attr.objects.filter(field = "SubsType").values('pk')
subssize_attr = Attr.objects.filter(field = "Size").values('pk')


class PizzaRate(models.Model):
    PizzaType = models.ForeignKey(Attr, on_delete = models.CASCADE, related_name = "pizza_type", limit_choices_to = { 'id__in' : pizzatype_attr})
    PizzaSize = models.ForeignKey(Attr, on_delete = models.CASCADE, related_name = "pizza_size", limit_choices_to = { 'id__in' : pizzasize_attr})
    ToppingType = models.ForeignKey(Attr, on_delete = models.CASCADE, related_name = "topping_type", limit_choices_to = { 'id__in' : toppingtype_attr})
    Price = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        unique_together = ["PizzaType", "PizzaSize", "ToppingType"]

    def __str__(self):
        return f"{self.PizzaSize} sized {self.PizzaType} pizza with {self.ToppingType} cost ${self.Price}"

class SubsRate(models.Model):
    SubsType = models.ForeignKey(Attr, on_delete = models.CASCADE, related_name = "subs_type", limit_choices_to = { 'id__in' : substype_attr})
    SubsChoice = models.CharField(max_length=64)
    SubsSize = models.ForeignKey(Attr, on_delete = models.CASCADE, related_name = "subs_size", limit_choices_to = { 'id__in' : subssize_attr})
    Price = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        unique_together = ["SubsType", "SubsChoice", "SubsSize"]

    def __str__(self):
        return f"{self.SubsType}: {self.SubsChoice} subs ({self.SubsSize} sized) cost ${self.Price}"

class PastaRate(models.Model):
    PastaChoice = models.CharField(max_length = 64)
    Price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return f"{self.PastaChoice} cost ${self.Price}"

class SaladsRate(models.Model):
    SaladsChoice = models.CharField(max_length = 64)
    Price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return f"{self.SaladsChoice} cost ${self.Price}"

class DinnerPlattersRate(models.Model):
    DinnerPlattersChoice = models.CharField(max_length = 64)
    DinnerPlattersSize = models.ForeignKey(Attr, on_delete = models.CASCADE, related_name = "dinnerplatters_size", limit_choices_to = { 'id__in' : pizzasize_attr})
    Price = models.DecimalField(max_digits = 6, decimal_places = 2)

    def __str__(self):
        return f"{self.DinnerPlattersSize} sized {self.DinnerPlattersChoice} cost ${self.Price}"
