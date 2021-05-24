from django.conf.locale.en import formats as en_formats
from django.contrib import admin

from app212.models import *
from .tick_admin import TickAdmin
from .token_admin import TokenAdmin
from .user_admin import UserAdmin

# Register your models here.
en_formats.DATETIME_FORMAT = "M d, Y H:i:s e"

admin.site.register(User, UserAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Tick, TickAdmin)

admin.site.site_title = "App212. System."
