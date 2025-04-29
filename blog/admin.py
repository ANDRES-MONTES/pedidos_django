from django.contrib import admin
from blog.models import Categoria, Post

# Register your models here.

@admin.register(Categoria)
class Admi_Categoria(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


@admin.register(Post)
class Admin_post(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')