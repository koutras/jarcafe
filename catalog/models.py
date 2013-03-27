from django.db import models

# Create your models here.

class Photo_album(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True,
		help_text='Unique value for product page URL, created from name.')
	description = models.TextField()
	is_active = models.BooleanField(default=True)
	meta_keywords = models.CharField("Meta Keywords", max_length=255,
		help_text='Comma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField("Meta Description", max_length=255,
		help_text='Content for description meta tag')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		db_table = 'photo_album'
		ordering = ['-created_at']
	
	def __unicode__(self):
		return self.name

	@models.permalink
	def get_absolute_url(self):
		return('catalog_photo_album', (), {'photo_album_slug':self.slug})
		

class Photo_frame(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True,
		help_text='Unique value for product page URL, created from name.')
	description = models.TextField()
	meta_description = models.CharField("Meta Description", max_length=255,
		help_text='Content for description meta tag')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	photo_album = models.ManyToManyField(Photo_album)
	image = models.ImageField(upload_to='images/bulk/')
	thumbnail = models.ImageField(upload_to='images/bulk/thumbnails')

	@models.permalink
	def get_absolute_url(self):
		return('catalog_photo_frame', (), {'photo_frame_slug' :self.slug})
	
	
	class Meta:
		db_table = 'photo_frame'
		ordering = ['-created_at']
	
	def __unicode__(self):
		return self.name
