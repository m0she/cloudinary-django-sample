from django.shortcuts import render

from .models import Photo
from .forms import PhotoForm

def filter_nones(d):
    return dict((k,v) for k,v in d.iteritems() if v is not None)

def list(request):
    defaults = dict(format="jpg", height=150, width=150)
    defaults["class"] = "thumbnail inline"

    samples = [
        dict(crop="fill", radius=10),
        dict(crop="scale"),
        dict(crop="fit", format="png"),
        dict(crop="thumb", gravity="face"),
        dict(format="png", angle=20, height=None, width=None, transformation=[
            dict(crop="fill", gravity="north", width=150, height=150, effect="sepia"),
        ]),
    ]
    samples = [filter_nones(dict(defaults, **sample)) for sample in samples]
    return render(request, 'list.html', dict(photos=Photo.objects.all(), samples=samples))

def upload(request):
    context = dict(backend_form = PhotoForm())
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        print form.instance, form.data
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'upload.html', context)

def direct_upload_complete(request):
    pass
