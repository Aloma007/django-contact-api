from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# NEW SWAGGER IMPORTS
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# IMPORTED TWO NEW TOOLS FOR MEDIA
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')),  # Your existing dispatch rider
# NEW SWAGGER ROUTES
    # 1. This generates the raw blueprint of your API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # 2. This creates the beautiful interactive website using the blueprint!
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # EXISTING SECURITY GATES
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# --- 2. OPEN ROUTE TO SERVE IMAGES DURING DEVELOPMENT ---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)