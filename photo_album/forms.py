from django.forms import ModelForm

from cloudinary.forms import CloudinaryJsFileField

from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo

class PhotoDirectForm(PhotoForm):
    image = CloudinaryJsFileField()
