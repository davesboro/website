from django.conf.urls import url
from . import views

app_name = 'spuds'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/2/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.PotatoCreate.as_view(), name='potato-add'),

    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.PotatoUpdate.as_view(), name='potato-update'),

    # /music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.PotatoDelete.as_view(), name='potato-delete'),
]