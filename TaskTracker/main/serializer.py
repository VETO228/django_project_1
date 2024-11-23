from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Task, RegisterUser, Projects, ProjectMember


class LogSerializer(serializers.Serializer):
    # Для авторизациии
    email = serializers.CharField()
    password = serializers.CharField()

    def validate_user(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
        attrs['user'] = user
        return attrs


class RegSerializer(serializers.ModelSerializer):
    # для регистрации
    password = serializers.CharField(min_length=12)

    class Meta:
        model = RegisterUser
        fields = ['email', 'username', 'surname']

    def save(self, **kwargs):
        user = RegisterUser()
        user.username = self.validated_data['username']
        user.surname = self.validated_data['surname']
        user.email = self.validated_data['email']
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = '__all__'
