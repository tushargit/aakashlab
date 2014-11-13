from django.conf.urls import patterns, include, url
from ac import views

urlpatterns = patterns(
    '',
    url(r'^$', views.all_ac, name='all_ac'),
    url(r'^iitb/$', views.iitb, name='iitb'),
    url(r'^(?P<id>\d+)/$', views.ac, name='ac'),

    url(r'^suggest_id/$', views.suggest_ac_id, name='suggest_ac_id'),
    url(r'^suggest_name/$', views.suggest_ac_name, name='suggest_ac_name'),
    url(r'^suggest_city/$', views.suggest_ac_city, name='suggest_ac_city'),
    url(r'^suggest_state/$', views.suggest_ac_state, name='suggest_ac_state'),
    url(r'^suggest_project/$', views.suggest_project_name,
        name='suggest_project_name'),

    url(r'^projects/$', views.projects, name='projects'),
    url(r'^project/(?P<id>\d+)/$', views.project, name='project'),
    url(r'^project/add/$', views.project_add, name='project_add'),
    url(r'^register/$', 'ac.views.register', name='register'),

    # Report in HTML
    url(r'^report/ac/$', 'ac.views.ac_report', name='ac_report'),
    url(r'^report/project/$', 'ac.views.project_report', name='project_report'),
    # Report in CSV
    url(r'^report/ac/csv/$', 'ac.views.csv_ac_report', name='csv_ac_report'),
    url(r'^report/project/csv/$', 'ac.views.csv_project_report',
        name='csv_project_report'),

)

