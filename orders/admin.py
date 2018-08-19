from django.contrib import admin
from .models import *

# Register your models here.
class OrderPizzaAdmin(admin.ModelAdmin):
    # filter_horizontal = ["toppingchoice",]
    list_display = ['user', 'pizzachoice', 'display_toppingchoice']
    list_filter = ['user']
    fieldsets = [
        ('User', {
            'fields': ['user']
        }),
        ('Order', {
            'fields': ['pizzachoice', 'toppingchoice']
        })
    ]
    filter_horizontal = ["toppingchoice",]

admin.site.register(Size)
admin.site.register(PizzaType)
admin.site.register(ToppingType)
admin.site.register(ToppingChoice)
admin.site.register(SubChoice)
admin.site.register(PizzaRate)
admin.site.register(SubRate)
admin.site.register(SubExtraRate)
admin.site.register(PastaRate)
admin.site.register(SaladRate)
admin.site.register(DinnerPlatterRate)
admin.site.register(OrderPizza, OrderPizzaAdmin)
admin.site.register(OrderSub)
admin.site.register(OrderPasta)
admin.site.register(OrderSalad)
admin.site.register(OrderDinnerPlatter)
