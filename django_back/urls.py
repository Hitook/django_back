from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

admin.site.site_header =  "Trivia Admin"  
admin.site.site_title  =  "Trivia admin site"
admin.site.index_title =  "Trivia Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/token/login', include('djoser.urls.authtoken')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/', include('trivia.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
