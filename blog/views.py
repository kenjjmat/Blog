from django.shortcuts import render
# database model
from .models import Post
from django.views.generic import ListView


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # the format needed for the template is <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['- date_posted']


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def new(request):
    return render(request, 'blog/new.html')
