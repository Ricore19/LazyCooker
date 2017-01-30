from django.conf.urls import url
from . import views_account
from . import views
from . import views_forum

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', views_account.connexion),
    url(r'^logout/$', views_account.deconnexion),
    url(r'^subscription/$', views_account.subscription),
    url(r'^profile/(?P<name>\w+)/$', views_account.profile),
    url(r'^changeprofile/$', views_account.changeprofile),
    url(r'^changepassword/$', views_account.changepassword),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
    url(r'^message/(?P<name>\w+)/$', views_account.message),
    url(r'^profile/(?P<name>\w+)/(?P<ide>\d+)/$', views_account.delmessage),
    url(r'^forum/$', views_forum.forumsection),
    url(r'^forum/section/(?P<ids>\d+)/(?P<page>\d+)/$', views_forum.forumpost),
    url(r'^forum/post/(?P<idp>\d+)/(?P<page>\d+)/$', views_forum.forumpostdetail),
    url(r'^forum/post/(?P<idp>\d+)/(?P<page>\d+)/like/$', views_forum.forumpostlike),
    url(r'^forum/post/(?P<idp>\d+)/(?P<page>\d+)/dislike/$', views_forum.forumpostdislike),
    url(r'^forum/post/(?P<idp>\d+)/(?P<page>\d+)/delcom/(?P<idc>\d+)/$', views_forum.forumpostdelcomment),
    url(r'^forum/postdel/(?P<idp>\d+)/$', views_forum.forumpostdel),
    url(r'^forum/postcreate/(?P<ids>\d+)/$', views_forum.forumpostcreate)
]
