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

##################### Inline Documentation ################

class InventoryPresentInline(admin.StackedInline):
	model = InventoryPresent
	extra = 2
	fields = ['item_name', 'quantity',]
	readonly_fields = ['date', 'brand','category', 'picture']


class InventoryIssuedInline(admin.StackedInline):
	model = InventoryIssued


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
	list_display = ['item_name', 'quantity','brand', 'storage_picture']
	list_editable = ['quantity']
	list_filter = ['category']
	search_fields = ['item_name']
	# inlines = [InventoryIssuedInline,]

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

	list_display = ['name','user_type','get_item_name','item_status']
	list_filter = ['user_type',]
	ordering = ['user_type',]
	search_fields = ['get_users', 'item_name']
	readonly_fields = ['user',]
	save_as = True
	filter_horizontal = ('get_users',)
	inlines = [InventoryPresentInline,]

	fields = (
		('name',),
		('user_type','get_users'),
		('item_status','user')
	)

	def get_item_name(self, obj):
		return ",\n".join([p.item_name for p in obj.item_name.all()])

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


































