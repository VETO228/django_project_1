from django.urls import path
from main import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('create_project/', views.ProjectsListView.as_view(), name='create_project'),
    path('projects/', views.ProjectList.projectlist, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:pk>/update/', views.project_update, name='project_update'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('project/<int:pk>/comment/', views.project_add_comment, name='project_add_comment'),

    path('create_task/', views.TaskListView.as_view(), name='create_task'),
    path('tasks/', views.TaskList.tasklist, name='task'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/comment/', views.task_add_comment, name='task_add_comment'),
]