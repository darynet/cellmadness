# coding: utf-8
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from blog.models import Post

#def news(request):
#    vars = dict (
#            posts=Post.objects.all().order_by('-datetime')[:5],
#               )
#
#   return render_to_response('blog/post_list.html', vars, context_instance=RequestContext(request))

def news(request):
    posts_list = Post.objects.all().order_by('-datetime')
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    vars = dict(
        posts=posts,
        )
    return render_to_response('blog/post_list.html', vars, context_instance=RequestContext(request))


def one_new(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    vars = dict(
        title=post.title,
        content=post.content,
        datetime=post.datetime,
    )

    return render_to_response('blog/post_detail.html', vars, context_instance=RequestContext(request))