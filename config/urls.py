from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('auth/',include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/',include('shell.urls')),
    path('admin/', admin.site.urls),
]
