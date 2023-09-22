from drf_yasg import openapi
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Seazone Code Challenge",
        default_version='v1',
        description="Seazone Code Challenge - APIs Backend Vacancy Python Developer",
        contact=openapi.Contact(email="yghorcastello.backend@gmail.com"),
        license=openapi.License(name="Yghor Castello - Dev Backend"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('core.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)