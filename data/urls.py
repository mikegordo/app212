from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/', include('app212.urls')),
    path('', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
