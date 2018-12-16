from django.contrib import admin
from .models import Post,Category,Tag
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title','created_time','modified_time','category','author']
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

