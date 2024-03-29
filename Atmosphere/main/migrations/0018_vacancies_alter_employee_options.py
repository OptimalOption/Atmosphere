# Generated by Django 4.0.2 on 2022-04-09 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_postimage_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('body', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('responsibilities', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Обязанности')),
                ('type_of_employment', models.CharField(blank=True, max_length=50, null=True, verbose_name='Тип занятости')),
                ('schedule', models.CharField(blank=True, max_length=50, null=True, verbose_name='График работы')),
                ('education', models.CharField(blank=True, max_length=50, null=True, verbose_name='Образование')),
                ('experience', models.CharField(blank=True, max_length=50, null=True, verbose_name='Стаж работы')),
                ('salary', models.IntegerField(blank=True, null=True, verbose_name='Зарплата')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['id'], 'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
    ]
