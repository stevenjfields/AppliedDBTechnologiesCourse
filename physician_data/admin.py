from django.contrib import admin
from physician_data.models import Provider, Address

# Register your models here.
class ProviderAdmin(admin.ModelAdmin):
    pass

class AddressAdmin(admin.ModelAdmin):
    pass

admin.site.register(Provider, ProviderAdmin)
admin.site.register(Address, AddressAdmin)