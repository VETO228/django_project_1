from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Index.index, name='home'),
    path('about/', views.About.about, name='about'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('reg/', views.UserRegistrationView.as_view(), name='register'),
    path('user/', views.UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('send_message/', views.send_email_view),

    path('api/v1/', include('main.urls')),
    path('api/v2/drf-auth/', include('rest_framework.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)