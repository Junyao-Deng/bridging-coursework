from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('title','content','author','created_time','last_updated_time')