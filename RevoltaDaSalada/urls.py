from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RevoltaDaSalada.views.home', name='home'),
    # url(r'^RevoltaDaSalada/', include('RevoltaDaSalada.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.Index.as_view()),
    url(r'^posts$', views.Posts.as_view()),
    url(r'^importinsta$', views.ImportInstagram.as_view()),
    url(r'^importfb$', views.ImportFacebook.as_view()),
    url(r'^importtwitter$', views.ImportTwitter.as_view()),
)
