from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from store.views import CustomAuthToken


schema_view = get_schema_view(
   openapi.Info(
      title="API Магазина",
      default_version='v1',
      description="Документация для проекта магазина",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', TemplateView.as_view(template_name="frontend/index.html"), name='home'),
    path('cart/', TemplateView.as_view(template_name="frontend/cart.html"), name='cart'),
    path('register/', TemplateView.as_view(template_name="frontend/register.html"), name='register'),
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
    path('api/', include('cart.urls')),
    path('api/token/', CustomAuthToken.as_view(), name='api-token'),
    path('api/token/', CustomAuthToken.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('login/', TemplateView.as_view(template_name="frontend/login.html"), name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)