from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from registration.forms import RegistrationFormUniqueEmail
from django.conf import settings 

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('main.urls')),
    # url(r'^$', 'tweet.views.home', name='home'),
    # url(r'^tweet/', include('tweet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/register/$', 'registration.views.register', {'backend': 'registration.backends.default.DefaultBackend', 'form_class': RegistrationFormUniqueEmail}),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
