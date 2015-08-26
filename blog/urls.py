#coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
    url(r'^$', 'news', name='news'),
    url(r'^(?P<post_id>\d+)/$', 'one_new', name='one_new'),

)