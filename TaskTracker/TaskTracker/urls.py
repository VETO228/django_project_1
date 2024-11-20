from django.contrib import admin
from django.urls import path, include
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Index.index, name='home'),
    path('about/', views.About.about, name='about'),
    path('reg/', views.Register.register, name='register'),

    path('api/v1/', include('main.urls')),
    path('api/v2/drf-auth/', include('rest_framework.urls')),
]

