from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.forms import AccountCreationForm
from accounts.models import GeneralUser

UserModel = get_user_model()

@admin.register(GeneralUser)
class GeneralUserAdmin(UserAdmin):
    model = UserModel
    add_form = AccountCreationForm
    form = AccountCreationForm

    list_display = ('email','type', 'is_staff', 'is_active')
    list_filter = ('type', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    def profile_info(self, user):
        if user.is_business and hasattr(user, 'businessuser'):
            return user.businessuser.company_name
        elif user.is_individual and hasattr(user, 'individualuser'):
            return f"{user.first_name} {user.last_name}"
        return 'Not added yet'

    profile_info.short_description = 'Profile Info'