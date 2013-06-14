# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        return super(Index, self).get(*args, **kwargs)