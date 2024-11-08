from django.contrib import admin
from burgers.models import Burger, franchise

# Register your models here.
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass

@admin.register(franchise)
class FranchiseAdmin(admin.ModelAdmin):
    pass