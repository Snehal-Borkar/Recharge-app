from django.contrib import admin
from .models import Service_provider,Plan
# Register your models here.

class Service_provider_admin(admin.ModelAdmin):
    list_display=('id','name')

class Plan_admin(admin.ModelAdmin):
    list_display=('id','service_provider','price','talktime','data','validity','sms','other_details')
 
admin.site.register(Service_provider,Service_provider_admin)
admin.site.register(Plan,Plan_admin)