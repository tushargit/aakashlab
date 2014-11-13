from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ac.views.index', name='index'),
    url(r'^about/$', 'ac.views.about', name='about'),
    url(r'^compete/$', 'ac.views.compete', name='compete'),
    url(r'^contact/$', 'ac.views.contact', name='contact'),
    url(r'^gnu/$', 'ac.views.gnu', name='gnu'),
    url(r'^faqs/$', 'ac.views.faq', name='faq'),
    url(r'^pubs/$', 'ac.views.pubs', name='pubs'),
    url(r'^activities/$', 'ac.views.activities', name='activities'),
    url(r'^tutorials/$', 'ac.views.tutorials', name='tutorilas'),
    url(r'^news/$', 'ac.views.news', name='news'),
    url(r'^sitemap/$', 'ac.views.sitemap', name='sitemap'),
    url(r'^privacy/$', 'ac.views.privacy', name='privacy'),
    url(r'^others/$', 'ac.views.others', name='others'),
    url(r'^user/profile/$', 'ac.views.user_profile', name='profile'),
    url(r'^user/profile/edit/$', 'ac.views.user_profile_edit',
        name='profile_edit'),
    url(r'^ac/', include('ac.urls')),                       
    # url(r'^aakashlabs/', include('aakashlabs.foo.urls')),
    url(r'^login/$', 'ac.views.user_login', name='login'),
    url(r'^logout/$', 'ac.views.user_logout', name='logout'),
	
    url(r'^home/introduction/$', 'ac.views.introduction', name='introduction'),
    url(r'^home/proposal/$', 'ac.views.proposal', name='proposal'),
    url(r'^home/history/$', 'ac.views.history', name='history'),
    url(r'^home/configuration/$', 'ac.views.configuration', name='configuration'),
    url(r'^home/distribution/$', 'ac.views.distribution', name='distribution'),
    url(r'^home/training/$', 'ac.views.training', name='training'),
    url(r'^home/sidebar_projects/$', 'ac.views.sidebar_projects', name='sidebar_projects'),
    url(r'^home/research/$', 'ac.views.research', name='research'),
    url(r'^home/future/$', 'ac.views.future', name='future'),

    url(r'^user/password/change/$',
        'django.contrib.auth.views.password_change'),
    url(r'^user/password/change/done/$',
        'django.contrib.auth.views.password_change_done'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Finally add robot.txt
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robot.txt')),
)

if settings.DEBUG is False:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
         'serve',
        {'document_root': settings.MEDIA_ROOT}),)
