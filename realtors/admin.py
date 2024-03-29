from django.contrib import admin

from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','email','hire_date')
    list_display_links = ('id','name')
    search_fields = ('name',)
    list_per_page = 10
    list_filter = ('hire_date',)

admin.site.register(Realtor , RealtorAdmin)
