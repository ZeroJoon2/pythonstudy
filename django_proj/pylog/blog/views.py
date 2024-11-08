from django.shortcuts import render
from blog.models import Post

# Create your views here.
def post_list(request):
    post_all_query = Post.objects.all()

    context = {
        'post_all' : post_all_query,
    }
    return render(request, 'post_list.html', context)

