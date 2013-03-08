from django.shortcuts import render

from .models import Photo

def list(request):
    defaults = dict(format="jpg", height=150, width=150)
    defaults["class"] = "thumbnail inline"

    samples = [
        dict(crop="fill", radius=10),
        dict(crop="scale"),
        dict(crop="fit"),
        dict(crop="thumb", gravity="face"),
        dict(format="png", transformation=[
            dict(crop="fill", gravity="north", width=150, height=150),
            dict(effect="sepia"),
            dict(angle=20),
        ]),
    ]
    samples = [dict(defaults, **sample) for sample in samples]
    return render(request, 'list.html', dict(photos=Photo.objects.all(), samples=samples))

upload = list
