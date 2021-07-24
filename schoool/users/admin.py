from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdminConfig(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2')
            }
        ),
    )

    list_display = ('username','is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    


#admin.site.register(User)
admin.site.register(Teacher, UserAdminConfig)
admin.site.register(Student,UserAdminConfig)
admin.site.register(Parent,UserAdminConfig)
admin.site.register(TeacherMore)
admin.site.register(StudentMore)

#customizing admin
admin.site.site_header = "Sacred Hearts"
admin.site.site_title = "Sacred Admin Portal"
admin.site.index_title = "Welcome to Sacred Admin Portal"
