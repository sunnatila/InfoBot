from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),  # This will allow access to the admin without the language code
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

