from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# import logging

# Set up the logger
# logger = logging.getLogger('django')

# Log when URLs are loaded
# logger.info("URL configuration loaded successfully")

schema_view = get_schema_view(
    title="API Documentation",
    permission_classes=[AllowAny],  # Disable authentication for this view
    authentication_classes=[],  # Remove authentication for schema view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', schema_view, name='schema'),
    # path('docs/', include_docs_urls(title='API Documentation')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
