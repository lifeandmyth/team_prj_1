from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post


# def home(request):
#   posts = Post.objects.all().order_by('-pk')
#   # 오름차순이면 pk, 내림차순이면 -pk (즉 최신게시물을 상단에 올리려면 내림차순인 -pk)
#   print(posts)
#   return render(request, 'blog/home.html',
#     {
#       'posts' : posts,
#     }              
#   )

class PostList(ListView):
  # 데이터를 가져올 queryset
  model = Post
  # 해당 기본키primary key값에 해당되는 Post 내 업로드한 게시물 중 가장 최근 것(Post 레코드 중 pk값이 작은 순서)을 표시하기 위해 -pk로 선언.
  template_name = 'blog/home.html'
  