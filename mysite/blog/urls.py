from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='PostList'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='PostDetail'),
]
