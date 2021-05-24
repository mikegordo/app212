from .base_model_admin import BaseTokenAdmin


class TickAdmin(BaseTokenAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = ['id', 'item_owner_link', 'owner_active', 'created']
    fields = ['id', 'item_owner_link', 'owner_active', 'payload', 'created']
    readonly_fields = ['id', 'item_owner_link', 'owner_active', 'payload', 'created']
    ordering = ['-created']

    def owner_active(self, token):
        return token.user.is_active

    owner_active.boolean = True
    owner_active.short_description = "User active"
