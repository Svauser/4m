from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import Users


@admin.register(Users)
class UsersAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username',
                            'password',
                            'avatar',
                            'age',
                            'bio')}),
        ('Permissions', {'fields': ('is_active',
                                        'is_staff',
                                        'is_superuser',
                                        'groups',
                                        'user_permissions')}),
        ('Important dates', {'fields': ('last_login',
                                         'date_joined')}),
    )

