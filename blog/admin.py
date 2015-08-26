# coding: utf-8
from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    models = Post
    list_display = ('title', 'datetime')
    list_filter = ('datetime',)

admin.site.register(Post, PostAdmin)