from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.List.as_view(), name='List'),
    #url(r'^(?P<codigo>[-\w]+)/$', views.Detail.as_view(), name='Detail'),
    url(r'^(?P<pk>\d+)/$', views.Detail.as_view(), name='Detail'),
]
