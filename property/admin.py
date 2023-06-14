from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address',)
    readonly_fields = ['created_at']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',
        ]
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by',]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'flat',
        'text',
        ]
    raw_id_fields = ['user', 'flat',]

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = [
        'full_name',
        'phone_number',
        'pure_phone',
        ]
    raw_id_fields = ['flat',]

# admin.site.register(Complaint)
