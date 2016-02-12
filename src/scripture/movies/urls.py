from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<slug>[\w\-]+)/$', views.detail, name='detail'),
  url(r'^tag/(?P<tag>[\w\-]+)/$', views.tag, name='tag')
]