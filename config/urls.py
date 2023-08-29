# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Project
from config.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls'), name='main'),

    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += doc_urls

urlpatterns += tuple(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns += tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
