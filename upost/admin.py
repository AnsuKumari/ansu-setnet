from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'created', 'modified')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'text', 'created')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
