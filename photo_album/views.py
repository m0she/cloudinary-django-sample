import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from cloudinary.forms import cl_init_js_callbacks

from .models import Photo
from .forms import PhotoForm, PhotoDirectForm

def filter_nones(d):
    return dict((k,v) for k,v in d.iteritems() if v is not None)

def list(request):
    defaults = dict(format="jpg", height=150, width=150)
    defaults["class"] = "thumbnail inline"

    # The different transformations to present
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

def upload(request, pk=None):
    instance = Photo.objects.get(pk=pk) if pk else None
    context = dict(save_pk = pk or "")
    if request.method == 'POST':
        # Only backend upload should be posting here
        context['backend_form'] = form = PhotoForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            # Uploads image and creates a model instance for it
            context['posted'] = form.save()

        instance = Photo.objects.get(pk=pk) if pk else None
    else:
        # Form demonstrating backend upload
        context['backend_form'] = PhotoForm(instance=instance)

    # Form demonstrating direct upload
    context['direct_form'] = PhotoDirectForm(instance=instance)
    # When using direct upload - the following call in necessary to update the
    # form's callback url
    cl_init_js_callbacks(context['direct_form'], request)

    return render(request, 'upload.html', context)

@csrf_exempt
def direct_upload_complete(request, pk=None):
    instance = Photo.objects.get(pk=pk) if pk else None
    form = PhotoDirectForm(request.POST, instance=instance)
    if form.is_valid():
        # Create a model instance for uploaded image using the provided data
        form.save()
        ret = dict(photo_id = form.instance.id)
    else:
        ret = dict(errors = form.errors)

    return HttpResponse(json.dumps(ret), content_type='application/json')
