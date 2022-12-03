# Generated by Django 4.0.2 on 2022-03-24 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_image_image_remove_new_photo_image_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Загрузить/Удалить изображение',
            },
        ),
        migrations.RenameModel(
            old_name='New',
            new_name='Post',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='main.post'),
        ),
    ]