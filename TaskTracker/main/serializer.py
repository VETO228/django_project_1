from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Task, RegisterUser, Projects, TaskComment, ProjectsComment


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = RegisterUser
        fields = ('username', 'surname', 'password', 'avatar', 'role', 'projects', 'token', 'email')

    def create(self, validated_data):
        user = RegisterUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None:
            raise serializers.ValidationError(
                'Поле почты не было заполено'
            )

        if password is None:
            raise serializers.ValidationError(
                'Поле пароля не было заполено'
            )

        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'Пользователь не определён'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        write_only=True
    )

    class Meta:
        model = RegisterUser
        fields = ('email', 'username', 'surname', 'password', 'token', 'avatar', 'role', 'projects',)
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = ['user', 'content', 'created_at']

class ProjectsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsComment
        fields = ['user', 'content', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

    def create(self, validated_data):
        project = Projects(**validated_data)
        project.save()
        return project
