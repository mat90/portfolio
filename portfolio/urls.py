from django.conf.urls import patterns, include, url
from apps.site.views import Home
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
