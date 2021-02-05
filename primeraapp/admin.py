from django.contrib import admin
from .models import Post
# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish', 'status')
    list_filter = ('title', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    ordering = ['status', 'publish',]
    prepolutaded_fields = {'slug': ('title',)}

admin.site.register(Post,postAdmin)
