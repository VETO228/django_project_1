from .models import Task, RegisterUser
from django import forms
from django.core.files.images import get_image_dimensions

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = RegisterUser
        fields = ('email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

