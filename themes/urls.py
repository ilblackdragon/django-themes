try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url # Django < 1.4

urlpatterns = patterns('themes.views',
    url('^change/$', 'change', name='themes_change'),
    url('^change/(?P<theme_id>[\d]+)/$', 'change', name='themes_change_id'),
)
