from .models import Task, RegisterUser
from django import forms
from django.core.files.images import get_image_dimensions

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = RegisterUser
        fields = ('email', 'username')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']
        try:
            width, height = get_image_dimensions(avatar)
            if width > height:
                raise forms.ValidationError(
                    '''Ширина больше высоты'''
                )
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(
                    '''Формат изображения не соответсвует сайту'''
                )
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    '''Не подходящий формат'''
                )
        except AttributeError:
            """
            Ошибка атрибута
            """
            pass
        return avatar


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

