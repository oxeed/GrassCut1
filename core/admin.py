from django.contrib import admin

# Register your models here.
from .models import Client



class ClientAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp']
    class Meta:
        model = Client



admin.site.register(Client, ClientAdmin)