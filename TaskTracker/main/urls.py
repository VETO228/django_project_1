from django.urls import path
from main import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('tasklist/', views.TaskAPIView.as_view(), name='tasklist'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('projects/', views.ProjectListCreateView.as_view(), name='project_list_create'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('project_members/', views.ProjectMemberListCreateView.as_view(), name='project_member_list_create'),
    path('project_members/<int:pk>/', views.ProjectMemberDetailView.as_view(), name='project_member_detail'),
]