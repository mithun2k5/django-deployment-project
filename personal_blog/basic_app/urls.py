from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^home/$',views.home,name='home'),
    url(r'^blog/$',views.blog,name='blog'),
    url(r'^blog/post1$',views.post1,name='post1'),
    url(r'^blog/post2/$',views.post2,name='post2'),
    url(r'^blog/post3/$',views.post3,name='post3'),
    url(r'^education/$',views.education,name='education'),
    url(r'^experience/$',views.experience,name='experience'),
    url(r'^certifications/$',views.certifications,name='certifications'),
    url(r'^skill/$',views.skill,name='skill'),
    url(r'^activities/$',views.activities,name='activities'),
    url(r'^projects/$',views.projects,name='projects'),
    url(r'^project1/$',views.project1,name='project1'),
    url(r'^project2/$',views.project2,name='project2'),
    url(r'^project3/$',views.project3,name='project3'),
    url(r'^project4/$',views.project4,name='project4'),
    url(r'^timezoneconversion/$',views.timezoneconversion,name='timezoneconversion'),
    url(r'^changereturn/$',views.changereturn,name='changereturn'),
    url(r'^subnetcalculator/$',views.subnetcalculator,name='subnetcalculator'),
    url(r'^binarytodecimal/$',views.binarytodecimal,name='binarytodecimal'),
    url(r'^decimaltobinary/$',views.decimaltobinary,name='decimaltobinary'),
    url(r'^whois/$',views.whois,name='whois'),
    ]
