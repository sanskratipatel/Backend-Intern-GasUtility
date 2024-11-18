# support/admin.py

from django.contrib import admin
from .models import SupportRequest

class SupportRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'email', 'phone', 'request_details', 'status')
    list_filter = ('status',)
    search_fields = ('customer_name', 'email', 'phone', 'request_details')

admin.site.register(SupportRequest, SupportRequestAdmin)
