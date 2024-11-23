from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Index.index, name='home'),
    path('about/', views.About.about, name='about'),
    path('reg/', views.Register.register, name='register'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),
    path('tasks/', views.task_list, name='task'),

    path('api/v1/', include('main.urls')),
    path('api/v2/drf-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)