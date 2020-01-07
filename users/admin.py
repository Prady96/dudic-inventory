from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group
from django.utils.safestring import mark_safe
from image_cropping import ImageCroppingMixin

import pdb
from django.utils.functional import SimpleLazyObject
from django.contrib import auth

###################### DEFAULT ############################
admin.site.site_header = 'DUDIC'
admin.site.site_title = 'DUDIC'
admin.site.index_title = 'Inventory Panel'
admin.site.unregister(Group)

##################### Inventory Issued ###################

@admin.register(RoleOfUser)
class RoleOfUserAdmin(admin.ModelAdmin):
	pass


@admin.register(InventoryPresent)
class PresentAdmin(admin.ModelAdmin, ImageCroppingMixin):

	readonly_fields = ['user',]

	fields = (
		('item_name', 'quantity'),
		('picture','category'),
		('brand','user'),
	)

	ordering = ['item_name','category']
	list_display = ['item_name', 'quantity','brand']
	list_editable = ['quantity']
	list_filter = ['category']
	search_fields = ['item_name']

	def storage_picture(self, obj):
		return mark_safe('<img src="{url}" width="100" height=100 />'.format(
            url = obj.picture.url,
            )
		)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)

@admin.register(InventoryIssued)
class IssuedAdmin(admin.ModelAdmin):

	list_display = ['get_users','get_user_type']
	list_filter = ['get_user_type',]
	ordering = ['get_user_type',]
	search_fields = ['get_users', 'item_name__item_name']
	readonly_fields = ['user',]
	save_as = True
	filter_horizontal = ('item_name',)

	fields = (
		('get_user_type','get_users'),
		('item_name', 'quantity'),
		('item_status','user')
	)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()
		# super().save_model(request, obj, form, change)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

	fields = (
		('username', 'email'),
		('name','user_type'),
		('phone_number'),
		('is_active','is_superuser','is_staff')
	)




admin.site.register(Categorie)


































