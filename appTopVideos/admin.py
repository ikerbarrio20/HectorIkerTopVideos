from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Video, Categoria, Plataforma
admin.site.register(Video)
admin.site.register(Categoria)
admin.site.register(Plataforma)
