from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }

    return render(request, 'posts/posts.html', context)


def post_detail(request,id):
    tmp = Post.objects.get(id = id)
    post_id = tmp.id
  
    post = get_object_or_404(Post, id = post_id)
    print(f'request.headers : {request.headers}')
    print(f"request.headers.get('Accept') : {request.headers.get('Accept')}")

    if request.headers.get('Accept') == 'application/json':
        print('accept')
        return JsonResponse({
            'title' : post.title,
            'content' : post.content
        })
    else:
        print('else')
        return render(request, 'posts/posts_detail.html', {'post_id':post_id})