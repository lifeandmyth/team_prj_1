from django.contrib import admin
from .models import Post
# summernote 관련 라이브러리
# from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(admin.ModelAdmin):
  fields = ('title', 'hook_text', 'content', 'created_at', 'updated_at', 'author', )

admin.site.register(Post, PostAdmin)