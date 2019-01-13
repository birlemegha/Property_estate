from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id','name','email','phone','hire_date')
	list_display_links = ('name','email')
	search_fields = ('name',)
	list_per_page = 25


admin.site.register(Realtor,RealtorAdmin)
