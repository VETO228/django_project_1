from models import Task
from django import forms
from django.core.files.images import get_image_dimensions


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'task',
            'link_proj',
            'link_author',
            'status',
            'priority',
            'date_create',
            'date_update',
            'period_execution',
            'tester',
        )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = RegisterUser
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