from django.contrib import admin
from .models import Articles, User


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'content', 'created_at', 'updated_at', 'is_public']
    search_fields = ['content']
    list_editable = ['is_public']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'password', 'group']


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(User, UserAdmin)
