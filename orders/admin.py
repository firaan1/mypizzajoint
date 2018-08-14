from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Size)
admin.site.register(PizzaType)
admin.site.register(ToppingType)
admin.site.register(ToppingChoice)
admin.site.register(SubExtra)
admin.site.register(PizzaRate)
admin.site.register(SubRate)
admin.site.register(PastaRate)
admin.site.register(SaladRate)
admin.site.register(DinnerPlatterRate)
