from django.contrib import admin

from .models import Attr, PizzaRate, SubsRate, PastaRate, DinnerPlattersRate
# Register your models here.

admin.site.register(Attr)
admin.site.register(PizzaRate)
admin.site.register(SubsRate)
admin.site.register(PastaRate)
admin.site.register(DinnerPlattersRate)
