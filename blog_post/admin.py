from django.contrib import admin
from .models import Post, Comment, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', )


admin.site.register(Comment, CommentAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Tag, TagAdmin)
