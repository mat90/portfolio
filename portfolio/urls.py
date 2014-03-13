from django.conf.urls import patterns, include, url
from apps.home.views import Home
from django.contrib import admin
from settings import MEDIA_ROOT
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': MEDIA_ROOT}),

    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
