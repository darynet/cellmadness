# coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.views import Post


# можно переписать как в news/views.py
def home(request):
    vars = dict (
            posts=Post.objects.all().order_by('-datetime')[:5],
                )

    return render_to_response('blog/index.html', vars, context_instance=RequestContext(request))
