from django.contrib import admin
from .models import PriceCard, PriceTable


# Register your models here.
class BoxPriceAdmin(admin.ModelAdmin):
    list_display = ('pc_value', 'type_price', 'pc_description')


class TableAdmin(admin.ModelAdmin):
    list_display = ('pt_title', 'pt_old_price', 'pt_new_price')


admin.site.register(PriceTable, TableAdmin)
admin.site.register(PriceCard, BoxPriceAdmin)
