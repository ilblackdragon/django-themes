from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('themes.views',
    url('^change/$', 'change', name='themes_change'),
    url('^change/(?P<theme_id>[\d]+)/$', 'change', name='themes_change_id'),
)