from django.contrib import admin

from order.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['size','order_status','quantity','created_at','updated_at']
    list_filter = ['created_at','size'] 