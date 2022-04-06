from django.contrib import admin
from .models import recharge

# Register your models here.

@admin.register(recharge)

class rechargeAdmin(admin.ModelAdmin):
    list_display=('id','number','provider','plans')
