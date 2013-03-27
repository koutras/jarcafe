from django import forms
from catalog.models import Photo_frame 

class Photo_frameAdminForm(forms.ModelForm):
	class Meta:
		model = Photo_frame 

	def clean_price(self):
		if self.cleaned_data['price'] <= 0:
			raise forms.ValidationError('Price must be greater than zero.')
		return self.cleaned_data['price']
