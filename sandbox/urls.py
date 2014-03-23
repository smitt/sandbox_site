from django.conf.urls import patterns, include, url
from django.conf import settings
from sandbox import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sandbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin/', views.signin),
    url(r'^signup/', views.signup),
    url(r'^forget_pass/', views.forget_pass),
    url(r'^about/', views.about),
    url(r'^', views.index)
)

if settings.DEBUG:
   urlpatterns += patterns('django.views.static', (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}), )
   #debug tool
   import debug_toolbar
   urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
