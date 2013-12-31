from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ac.views.index', name='index'),
    url(r'^about/$', 'ac.views.about', name='about'),
    url(r'^compete/$', 'ac.views.compete', name='compete'),
    url(r'^contact/$', 'ac.views.contact', name='contact'),
    url(r'^faqs/$', 'ac.views.faq', name='faq'),
    url(r'^pubs/$', 'ac.views.pubs', name='pubs'),
    url(r'^user/profile/$', 'ac.views.user_profile', name='profile'),
    url(r'^ac/', include('ac.urls')),                       
    # url(r'^aakashlabs/', include('aakashlabs.foo.urls')),
    url(r'^login/$', 'ac.views.user_login', name='login'),
    url(r'^logout/$', 'ac.views.user_logout', name='logout'),

    url(r'^user/password/change/$',
        'django.contrib.auth.views.password_change'),
    url(r'^user/password/change/done/$',
        'django.contrib.auth.views.password_change_done'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG is False:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
         'serve',
        {'document_root': settings.MEDIA_ROOT}),)
