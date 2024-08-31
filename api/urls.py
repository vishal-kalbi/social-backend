from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import RegisterView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

