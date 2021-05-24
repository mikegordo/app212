from django.contrib.admin import ModelAdmin
from django.urls import reverse_lazy
from django.utils.html import format_html


class BaseTokenAdmin(ModelAdmin):
    def item_owner_link(self, item):
        if not item.user:
            return None

        url = reverse_lazy('admin:%s_%s_change' % (item.user._meta.app_label,
                                                   item.user._meta.model_name),
                           args=(item.user.id,))

        return format_html(
            u'<a href="{}">{} - {}</a>'.format(url, item.user, item.user.get_full_name()))

    item_owner_link.short_description = "User"
