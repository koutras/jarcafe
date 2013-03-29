# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from catalog.models import Photo_album, Photo_frame
from django.template import RequestContext

def index(request, template_name="index.html"):
	page_title = ' Welcome to Jar!'
	return render_to_response(template_name, locals(),
		context_instance=RequestContext(request))

def show_album(request, photo_album_slug, template_name="photo_album.html"):	
	album = get_object_or_404(Photo_album, slug= photo_album_slug)   
	frames = album.photo_frame_set.all()
	meta_keywords = album.meta_keywords
	meta_description = album.meta_description 
	return render_to_response(template_nae, locals(), context_instance=RequestContext(request))

