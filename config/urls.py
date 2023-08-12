from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls'), name='main'),

    path("__debug__/", include("debug_toolbar.urls")),
]
