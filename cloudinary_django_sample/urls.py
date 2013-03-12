from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

import photo_album.views as photo_album

urlpatterns = patterns('',
    url(r'^$', photo_album.list),
    url(r'^list$', photo_album.list),
    url(r'^upload$', photo_album.upload),
    url(r'^upload/complete$', photo_album.direct_upload_complete),
    (r'^admin/', include(admin.site.urls)),
)
