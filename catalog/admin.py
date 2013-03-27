from django.contrib import admin
from catalog.models import Photo_album, Photo_frame 
from catalog.forms import Photo_frameAdminForm

class Photo_albumAdmin(admin.ModelAdmin):
		# sets values for how the admin site lists your products
	list_display = ('name', 'created_at', 'updated_at',)
	list_display_links = ('name',)
	list_per_page = 50
	ordering = ['-created_at']

	search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
#	exclude = ('created_at', 'updated_at',)

	# sets up slug to be generated from product name
	prepopulated_fields = {'slug' : ('name',)}

#registers you product model with the admin site
admin.site.register(Photo_album, Photo_albumAdmin)

class Photo_frameAdmin(admin.ModelAdmin):
	form = Photo_frameAdminForm
	#sets up values for how admin site lists categories
	list_display = ('name', 'created_at', 'updated_at',)
	list_display_links=('name',)
	list_per_page = 20
	ordering = ['name']
	search_fields = ['name', 'description', 'meta_keywords', 'meta_decription']

	# sets up slug to be generated from category name
	prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Photo_frame,Photo_frameAdmin)



