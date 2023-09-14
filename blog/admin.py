from django.contrib import admin
from blog.models import Post, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['likes', 'tags', 'author']
    llist_display = ['title', 'author']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'post']
    list_display = ['author', 'post', 'text']

admin.site.register(Tag)
