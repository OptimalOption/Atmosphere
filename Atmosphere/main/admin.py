from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'rank')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'rank')


class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_photo')
    list_display_links = ('id', 'admin_photo')

    def admin_photo(self, object):
        if object.img:
            return mark_safe(f"<img src='{object.img.url}' width=50>")

    admin_photo.short_description = "Изображение"


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, ImageAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(PostVideo, VideoAdmin)
admin.site.register(Slider, VideoAdmin)
admin.site.register(Vacancies, VacanciesAdmin)
