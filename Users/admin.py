from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA
from .models import User

# Register your models here.

#defining the class for how it looks like in admin panel because we are using a custom model 
class UserAdmin(UA):
    """Define admin model for custom User model with no email field."""

    fieldsets = ()
    add_fieldsets = ()
            
    list_display = ('email', 'first_name','is_staff','is_active','last_login','date_joined')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('id','date_joined','last_login')
    ordering = ('email',)


#registering the app
admin.site.register(User,UserAdmin)