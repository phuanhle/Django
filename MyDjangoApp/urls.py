from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from . import views,restful

urlpatterns = [
    #View static
    url(r'^$', TemplateView.as_view(template_name='html/index.html'), name="home"),
    url(r'^rest$', TemplateView.as_view(template_name='html/restful.html'), name="restful"),

    #View with define
    url(r'^search$', views.search, name='search'),    
    url(r'^update$', views.update, name='update'),
    url(r'^insert$', views.insert, name='insert'),    
    url(r'^delete$', views.delete, name='delete'),

    #Restful with define
    url(r'^rest/search/(?P<json_query>.+)/$', restful.search, name='search'),
    url(r'^rest/insert/$', restful.insert, name='insert'),                                                    
    
    #url(r'^rest/update/(?P<json_query>.+)/$', restful.update, name='update'),
    url(r'^rest/update/(?P<json_query>.+)/$', restful.update, name='update'),    
    url(r'^rest/delete/(?P<json_query>.+)/$', restful.delete, name='delete'),
    #Restful POST
        

    url(r'^age/(?P<question_id>[0-9*]+)/$', views.detail, name='detail'),
    #url(r'^age/(?P<question_id>)/$', views.detail, name='detail'),
 
]

