from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Blog
def blog_list(request):
    all_blogs = Blog.objects.all()
    return render(
        request,
        'blog/list.html',
        context=dict(blogs=all_blogs),
    )


def blog_detail(request, id):
    blogs = get_object_or_404(Blog, id=id)
    return render(
        request,
        'blog/post_detail.html',
        context=dict(blogs=blogs),
    )
