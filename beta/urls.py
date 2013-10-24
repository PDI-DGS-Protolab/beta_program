from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from register.views import index, join, thanks

import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beta.views.home', name='home'),
    # url(r'^beta/', include('beta.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    ######################################################
    # VIEWS
    ######################################################
    url(r'^$',       index),
    url(r'^join$',   join),
    url(r'^thanks$', thanks),

    ######################################################
    # ACCOUNTS
    ######################################################
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),

    ######################################################
    # ADMIN
    ######################################################

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    ######################################################
    # I18N
    ######################################################
    (r'^i18n/', include('django.conf.urls.i18n')),

    ######################################################
    # STATIC CONTENT
    ######################################################

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
)
