from django.shortcuts import render
from django.template.context_processors import request
from rest_framework import generics, status
from rest_framework.decorators import api_view

from .serializer import TaskSerializer, RegSerializer, ProjectSerializer, LogSerializer
from .models import Task, RegisterUser
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class Index:
    def index(request):
        return render(request, 'main/index.html')

class About:
    def about(request):
        return render(request, 'main/about.html')

class Regist:
    def regist(request):
        return render(request, 'main/register.html')


class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ProjectsAPIView(APIView):
    def get(self, request):
        return Response({'title': 'Projects'})


@api_view(['POST'])
def log_in_user(request):
    serializer = LogSerializer(data=request.data)
    # если указать в .is_valid(raise_exception=True),
    # то указывать условие не надо также, как и респонс после условия
    if serializer.is_valid():
        user = serializer.validated_data['user']
        if not user:
            return Response({"error": {"code": status.HTTP_401_UNAUTHORIZED,
                                       "message": "Authentication failed"}},
                            status=status.HTTP_401_UNAUTHORIZED)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'data': {"user_token": token.key}},
                        status=status.HTTP_200_OK)
    return Response({'error': {'code': status.HTTP_422_UNPROCESSABLE_ENTITY,
                               "message": "Validation error"}},
                    status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['POST'])
def sign_up_user(request):
    serializer = RegSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = Token.objects.create(user=user)
    return Response({'data': {"user_token": token.key}},
                    status=status.HTTP_201_CREATED)


@api_view(['POST'])
def log_out_user(request):
    if not request.user.is_active:
        return Response({"error": {"code": status.HTTP_403_FORBIDDEN,
                                   "message": "Login failed"}},
                        status=status.HTTP_403_FORBIDDEN)
    request.user.auth_token.delete()
    return Response({"data": {"message": "log out successfully"}},
                    status=status.HTTP_200_OK)
