# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
import importPost, models
from django.shortcuts import render

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        importPost.import_twitter()
        context['instagramPosts'] = models.InstagramPost.objects.all()
        #context['twitterPosts'] = models.TwitterPost.objects.all()
        return context