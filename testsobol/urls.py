from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from testsobol.mainapp.views import Index, Http, Edit

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Index.as_view()),
    url(r'^edit/$', Edit.as_view(), name="edit"),
    url(r'^http/$', Http.as_view(), name="http"),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        {"template_name": "admin/login.html"}),

    # url(r'^testsobol/', include('testsobol.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
