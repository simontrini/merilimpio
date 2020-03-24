from django.conf.urls import url, include
from django.contrib import admin
from inicio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^blog/', include('blog.urls')),
    url(r'^productos/', views.productos, name='productos'),
    url(r'^clientes/', views.clientes, name='clientes'),
    url(r'^contacto/', views.contacto, name='contacto'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
