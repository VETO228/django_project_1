from django.urls import path, include

from main import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import sign_up_user, log_in_user, log_out_user

urlpatterns = [
    path('tasklist', views.TaskAPIView.as_view(), name='tasklist'),
    path('projects', views.ProjectsAPIView.as_view(), name='projects'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('signup', sign_up_user),
    path('login', log_in_user),
    path('logout', log_out_user),
]