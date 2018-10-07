from django.contrib import admin
from .models import *

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
admin.site.register(PlacedOrder)
