import settings
from django.conf.urls.defaults import patterns, include, url



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$',
                         'django.views.static.serve', {
                              'document_root': settings.MEDIA_ROOT,
                              'show_indexes': True,
                              },
                         ),
)
