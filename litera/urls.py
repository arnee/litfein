from django.conf.urls import patterns, include, url
#from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.conf import settings
import os.path

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('feincms.urls')),
)


#if settings.DEBUG:
#    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#
#    urlpatterns += staticfiles_urlpatterns() # tell gunicorn where static files are in dev mode
#    urlpatterns += static(settings.MEDIA_URL + 'images/', document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
#    urlpatterns += patterns('',
#        (r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'demo/images/favicon.ico'))
#    )
