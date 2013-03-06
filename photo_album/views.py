from django.shortcuts import render

from .models import Photo

def list(request):
    return render(request, 'list.html', dict(photos = Photo.objects.all()))

upload = list
