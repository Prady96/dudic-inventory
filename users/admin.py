from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe
from image_cropping import ImageCroppingMixin

import pdb ## debugger
from django.utils.functional import SimpleLazyObject
from django.contrib import auth

from django import forms

###################### DEFAULT ######################################
admin.site.site_header 		= 'DUDIC'
admin.site.site_title 		= 'DUDIC'
admin.site.index_title 		= 'Inventory Panel'
admin.site.unregister(Group)

##################### Inline Code ##################################

class InventoryPresentInline(admin.StackedInline):
	model 			= InventoryPresent
	extra 			= 0
	fields 			= ['item_name', 'quantity','picture', 'item_status', 'brand',]
	# readonly_fields = []


##################### Actions Forms ( Sending Mails ) ##############
from django.views.generic.edit import FormView
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


class SendEmailForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('Subject')}))
    message = forms.CharField(widget=forms.Textarea)
    users = forms.ModelMultipleChoiceField(label="To",
                                           queryset=UserProfile.objects.all(),
                                           widget=forms.SelectMultiple())

# SendUserEmails view class
class SendUserEmails(FormView):
    template_name = 'users/send_email.html'
    form_class = SendEmailForm
    success_url = reverse_lazy('admin:users_user_changelist')

    def form_valid(self, form):
        users 			= form.cleaned_data['users']
        subject 		= form.cleaned_data['subject']
        message 		= form.cleaned_data['message']
        email_users.delay(users, subject, message)
        user_message 	= '{0} users emailed successfully!'.format(form.cleaned_data['users'].count())
        messages.success(self.request, user_message)
        return super(SendUserEmails, self).form_valid(form)

def sendMails(self, request, queryset):
	form = SendEmailForm(initial={'users': queryset})
	return render(request, 'template/send_email.html', {'form': form})

##################### Inventory Admin #############################

@admin.register(ItemNames)
class ItemNamesAdmin(admin.ModelAdmin):
	fields = (
		('name',),
	)



@admin.register(RoleOfUser)
class RoleOfUserAdmin(admin.ModelAdmin):
	pass


@admin.register(InventoryPresent)
class PresentAdmin(admin.ModelAdmin, ImageCroppingMixin):

	# readonly_fields = ['user',]

	fields = (
		('item_name', 'quantity'),
		('picture','category'),
		('brand','user'),
	)

	ordering 		= ['item_name','category']
	list_display 	= ['item_name', 'quantity','brand', 'storage_picture']
	list_editable 	= ['quantity']
	list_filter 	= ['category']
	search_fields 	= ['item_name']
	# inlines = [InventoryIssuedInline,]

	def storage_picture(self, obj):
		return mark_safe('<img src="{url}" width="100" height=100 />'.format(
            url = obj.picture.url,
            )
		)

	# def save_model(self, request, obj, form, change):
	# 	obj.user = request.user
	# 	super().save_model(request, obj, form, change)

@admin.register(InventoryIssued)
class IssuedAdmin(admin.ModelAdmin):

	list_display 		= ['name','user_type',]
	list_filter 		= ['user_type',]
	ordering 			= ['user_type',]
	search_fields 		= ['get_users', 'item_name']
	readonly_fields 	= ['user',]
	save_as 			= True
	filter_horizontal 	= ('get_users','item_name',)
	inlines 			= [InventoryPresentInline,]
	actions 			= [sendMails,]

	fields = (
		('name',),
		('user_type','get_users'),
		('item_name',),
        ('user'),
	)

	def get_item_name(self, obj):
		return ",\n".join([p.item_name for p in obj.item_name.all()])

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		# obj.save()
		super().save_model(request, obj, form, change)





@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

	fields = (
		('username', 'email'),
		('name','user_type'),
		('phone_number'),
		('is_active','is_superuser','is_staff')
	)

admin.site.register(Categorie)


































