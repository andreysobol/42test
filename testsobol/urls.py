from django.conf.urls.defaults import patterns, url
from testsobol.mainapp.views import Index, Http

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Index.as_view()),
    url(r'^http/$', Http.as_view(), name="http"),
    # url(r'^testsobol/', include('testsobol.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
