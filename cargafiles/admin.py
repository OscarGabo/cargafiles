from django.contrib import admin
from .models import File

# Register your models here.

#admin.site.register(File) 

@admin.register(File)
class AdminFiles (admin.ModelAdmin):
	list_display = ('id','nombre','fecha')
	list_filter = ('nombre',)
