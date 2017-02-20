from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^apartments/(?P<pk>[0-9]+)/$', views.questions_list, name='questions_list'),
]