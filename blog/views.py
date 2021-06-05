from django.shortcuts import render
from blog.models import Post, Category
from django.core.paginator import Paginator

# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    # ?page=2
    posts = paginator.get_page(page)
    context = {'posts': posts}
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        '-created_on'
    )
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'category': category,
        'posts': posts}
    return render(request, 'blog_categories.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'blog_detail.html', context)
