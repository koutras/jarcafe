from django.conf.urls.defaults import *

urlpatterns = patterns('catalog.views',
	(r'^$', 'index',{ 'template_name': 'index.html'}, 'catalog_home'),
	(r'^photo-album/(?P<photo_album_slug>[-\w]+)/$', 'show_album',
		{'template_name' : 'photo_album.html'}, 'catalog_album'),

	(r'^photo-frame/(?P<photo_frame_slug>[-\w]+)/$', 'show_frame',
		{'template_name' : 'photo_frame.html'}, 'catalog_photo_frame'),

#	(r'^/about/$', 'about',{'template_name' : 'about.html'}),
#	(r'^/contact/$', 'contact',{'template_name' : 'contact.html'}),

	
)

