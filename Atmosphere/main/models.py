from django.core.validators import FileExtensionValidator
from django.db import models


class Post(models.Model):
    title = models.CharField('Название', max_length=250)
    body = models.TextField('Описание', max_length=5000)
    created_at = models.DateTimeField('Время создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', '-id']


class Employee(models.Model):
    name = models.CharField('ФИО', max_length=250)
    rank = models.CharField('Звание', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        ordering = ['id']


class Slider(models.Model):
    name = models.CharField('Название', max_length=250, null=True)
    title = models.CharField('Заголовок', max_length=100, null=True, blank=True)
    text = models.CharField('Текст (ссылается на новости)', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'


class Vacancies(models.Model):
    title = models.CharField('Название', max_length=250, null=True)
    body = models.TextField('Описание', max_length=1000, null=True, blank=True)
    responsibilities = models.TextField('Обязанности', max_length=1000, null=True, blank=True)
    type_of_employment = models.CharField('Тип занятости', max_length=50, null=True, blank=True)
    schedule = models.CharField('График работы', max_length=50, null=True, blank=True)
    education = models.CharField('Образование', max_length=50, null=True, blank=True)
    experience = models.CharField('Стаж работы', max_length=50, null=True, blank=True)
    salary = models.IntegerField('Зарплата', null=True, blank=True)
    created_at = models.DateTimeField('Время создания', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-id']


class PostImage(models.Model):
    img = models.ImageField('Изображение', upload_to='photos/%Y/%m/%d/', null=True)
    post = models.ForeignKey(Post, related_name='Images', on_delete=models.SET_NULL, null=True, blank=True)
    employee = models.ForeignKey(Employee, related_name='Images', on_delete=models.SET_NULL, null=True, blank=True)
    slider = models.ForeignKey(Slider, related_name='Images', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class PostVideo(models.Model):
    name = models.CharField('Название', max_length=250, null=True)
    video = models.FileField('Видео', upload_to='videos/%Y/%m/%d/',
                             validators=[FileExtensionValidator(allowed_extensions=['mp4'])], null=True)
    post = models.ForeignKey(Post, related_name='Videos', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
