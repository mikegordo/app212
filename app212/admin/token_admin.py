from .base_model_admin import BaseTokenAdmin


class TokenAdmin(BaseTokenAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = ['token_shadow', 'created', 'last_used', 'times_used', 'item_owner_link', 'owner_active']
    fields = ['key', 'created', 'last_used', 'times_used', 'item_owner_link']
    search_fields = ['key', 'user__username', 'user__first_name', 'user__last_name', 'user__email']
    list_filter = ['times_used', 'last_used']
    readonly_fields = ['key', 'created', 'last_used', 'times_used', 'item_owner_link']
    ordering = ['-created']

    def token_shadow(self, token):
        return '*{}'.format(token.key[-4:].upper())

    token_shadow.short_description = "Token"

    def owner_active(self, token):
        return token.user.is_active

    owner_active.boolean = True
    owner_active.short_description = "User active"
