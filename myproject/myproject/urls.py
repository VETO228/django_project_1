from django.contrib import admin
from django.urls import path
from main import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('api/v1/tasklist/', views.TaskAPIView.as_view(), name='tasklist'),
    path('api/v2/reg/', views.RegisterAPIView.as_view(), name='register'),
    path('api/v3/projects/', views.ProjectsAPIView.as_view(), name='projects'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

