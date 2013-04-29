from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

import photo_album.views as photo_album

urlpatterns = patterns('',
    # URL for listing all images:
    url(r'^$', photo_album.list),
    url(r'^list$', photo_album.list),
    # URL for uploading an image
    url(r'^upload$', photo_album.upload),
    # The direct upload functionality reports to this URL when an image is uploaded.
    url(r'^upload/complete$', photo_album.direct_upload_complete),
    # Add the admin functionality:
    (r'^admin/', include(admin.site.urls)),
)
