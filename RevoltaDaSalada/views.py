# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import models, importPost, simplejson, datetime

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        posts = models.Post.objects.all()[:200]
        context['posts'] = posts
        return context

class JSONResponseMixin(object):

    def render_to_json(self, context, *args, **response_kwargs):
        data = simplejson.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
class Posts(TemplateView):
    template_name = 'posts.html'

    # def get(self, *args, **kwargs):
    #     return self.render_to_json(self.get_context_data())

    def get_context_data(self, **kwargs):
    	print "aquiiiiiiiiiiiiiiiiii"
        context = super(Posts, self).get_context_data(**kwargs)
        paginator = Paginator(models.Post.objects.all(), 12)
        page = self.request.GET.get('page', 1)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
            page = 1;
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)

        context["posts"] = posts.object_list
        context["page"] = page
        return context
