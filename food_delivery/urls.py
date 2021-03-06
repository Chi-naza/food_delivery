from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# r is the raw string literal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('API.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('food_delivery_web.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]

if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)