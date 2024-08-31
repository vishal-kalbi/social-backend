from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]
