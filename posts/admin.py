from django.contrib import admin
from.models import Post, Category, Tag, Comment
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_date', 'approved']
    list_filter = ['approved', 'created_date']
    search_fields = ['author', 'content']
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Одобрить выбранные комментарии"
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)