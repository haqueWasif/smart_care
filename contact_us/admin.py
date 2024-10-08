from django.contrib import admin
from .models import ContactUs

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'problem']

# Register your models here.
admin.site.register(ContactUs, ContactModelAdmin)
