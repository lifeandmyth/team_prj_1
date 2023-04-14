from django.db import models
# 사용자 필드 구현을 위한 호출
from django.contrib.auth.models import User
# django-markdownx 호출 -> 마크다운 문법 적용하기
from markdownx.models import MarkdownxField
# 마크다운 문법으로 작성된 content 필드 값을 HTML로 변환하기 위해 필요한 기능 호출
from markdownx.utils import markdown
import os

class Post(models.Model):
  title = models.CharField(max_length=30)

  hook_text = models.CharField(max_length=100, blank=True)
  # content = models.TextField()
  # django-markdownx를 적용한다면:
  content = models.TextField()


  created_at = models.DateTimeField(auto_now_add=True)

  updated_at = models.DateTimeField(auto_now=True)
  
  #on_delete=models.CASCADE 
  #이 포스트의 작성자가 데이터베이스에서 삭제되었을 때 이 포스트도 같이 삭제된다는 의미.
  
  #이 경우 사용자가 삭제되어도 그 사용자가 작성한 글은 남겨두고 author 필드 값만 null로 바뀌도록 설정.
  #null=True를 추가함으로써 원래 null이 될 수 없는(정확히는 허용치 않는) 필드값이 null이 될 수 있게 한다.
  author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)


