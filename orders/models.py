from django.db import models

# Create your models here.
class Attr(models.Model):
    field = models.CharField(max_length=25)
    value = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.value}"
        # return f"{self.field}: {self.value}"

pizzatype_attr = Attr.objects.filter(field = "PizzaType").values('pk')
pizzasize_attr = Attr.objects.filter(field = "Size").exclude(id__in = Attr.objects.filter(field = "Size", value = "None").values('pk')).values('pk')
toppingtype_attr = Attr.objects.filter(field = "ToppingType").values('pk')


class PizzaRate(models.Model):
    PizzaType = models.ForeignKey(Attr, on_delete = models.CASCADE, related_name = "pizza_type", limit_choices_to = { 'id__in' : pizzatype_attr})
    PizzaSize = models.ForeignKey(Attr, on_delete = models.CASCADE, related_name = "pizza_size", limit_choices_to = { 'id__in' : pizzasize_attr})
    ToppingType = models.ForeignKey(Attr, on_delete = models.CASCADE, related_name = "topping_type", limit_choices_to = { 'id__in' : toppingtype_attr})
    Price = models.DecimalField(max_digits = 6, decimal_places = 2)

    class Meta:
        unique_together = ["PizzaType", "PizzaSize", "ToppingType"]

    def __str__(self):
        return f"{self.PizzaSize} sized {self.PizzaType} pizza with {self.ToppingType} cost ${self.Price}"
