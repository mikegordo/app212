from django.contrib.admin import ModelAdmin


class UserAdmin(ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    readonly_fields = ['id', 'date_joined', 'last_login', 'username', 'created', 'updated']

    fieldsets = (
        (None, {'fields': ('id', 'username')}),
        ('PERSONAL INFO', {'fields': (('first_name', 'last_name'),
                                      'email')}),
        ('PERMISSIONS', {'fields': ('is_superuser', 'is_staff', 'is_active', 'is_deleted')}),
        ('MISCELLANEOUS', {'fields': (('created', 'updated'), 'date_joined', 'last_login')}),
    )
