from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
	 list_display= ('id', 'title', 'price', 'list_date', 'is_published','realtor')
	 list_display_links= ('id','title',)
	 list_filter = ('realtor',)
	 search_fields = ('title','realtor','price',)
	 list_editable = ('is_published',)
	 list_per_page =25


admin.site.register(Listing, ListingAdmin)
