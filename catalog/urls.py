from django.conf.urls.defaults import *

urlpatterns = patterns('catalog.views',
	(r'^$', 'index', { 'template_name': 'index.html'}, 'catalog_home'),
	(r'^photo-album/(?P<photo-album>[-\w]+)/$', 'show_album',
		{'template_name' : 'photo_album.html'}, 'catalog_album'),
	(r'^/about/$', 'about',{'template_name' : 'about.html'}),
	(r'^/contact/$', 'contact',{'template_name' : 'contact.html'}),
	
)

