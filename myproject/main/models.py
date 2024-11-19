from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager
from django.core.validators import FileExtensionValidator
from django.db import models



class RegisterUser(AbstractUser):
    name = models.CharField('Имя пользователя', max_length=100, blank=True, null=True)
    surname = models.CharField('Фамилия пользователя', max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
    )
    character = models.CharField('Роль на платформе', max_length=100, blank=True, null=True)
    project = models.FileField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()
    REQUIRED_FIELDS = ['username']


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')
    link_proj = models.FileField('Проект')
    link_author = models.CharField('Автор', max_length=100)
    status = models.CharField('Статус',
        choices=[("Grooming", "Grooming"), ("In Progress", "In Progress"), ('Dev', 'Dev'), ('Done', 'Done')],
        max_length=100)
    priority = models.CharField('Приоритет', max_length=100, blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now=True)
    period_execution = models.DateTimeField('Срок выполнения', blank=True, null=True)
    tester = models.CharField('Ответственный за тестировку', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'


class UserManagers(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, fio, email, password, **extra_fields):
        if not email:
            raise ValueError('Адрес электронной почты должен быть установлен')
        email = self.normalize_email(email)
        user = self.model(fio=fio, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, fio, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(fio, email, password, **extra_fields)

    def create_superuser(self, fio, email=None, password=None,
                         **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(fio, email, password, **extra_fields)


    @property
    def is_authenticated(self):
        """Всегда возращает True. Это способ узнать, был ли пользователь аутентифицированы
        """
        return True


    def __str__(self):
        return self.name


    class Meta:
        pass



class Projects(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.CharField('Статус', choices=[('Активен', 'Активен'), ('Архивирован', 'Архивирован')] ,max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        pass

