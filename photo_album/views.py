import json

from django.core.urlresolvers import reverse
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
    context = dict(
        backend_form = PhotoForm(),
        direct_form = PhotoDirectForm(),
        upload_callback = request.build_absolute_uri(reverse('photo_album.views.upload')),
    )
    cl_init_js_callbacks(context['direct_form'], request)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()

    return render(request, 'upload.html', context)

@csrf_exempt
def direct_upload_complete(request):
    form = PhotoDirectForm(request.POST.copy())
    if form.is_valid():
        form.save()
        ret = dict(photo_id = form.instance.id)
    else:
        ret = dict(errors = form.errors)

    return HttpResponse(json.dumps(ret), content_type='application/json')
